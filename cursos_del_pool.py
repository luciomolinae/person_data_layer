from logger_base import log
from conexion import Conexion

class CursorDelPool:
    def __int__(self):
        self._conexion = None
        self._cursor = None

    def __enter__(self): # entramos a la ejecuccion de bloque with solicitamos un objeto conexion y cursor
        log.debug(f'Inicio del metodo with __enter__')
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor

    def __exit__(self, tipo_excepcion, valor_excepcion, detalle_exepcion): # cuando terminamos el bloque with verificamos si hubo alguna excepcion
        log.debug('Se ejecuta metodo __exit__')
        if valor_excepcion:
            self._conexion.rollback() # si hubo exepcion se hace rollback y vemos como corregirla
            log.error(f'Ocurrio una excepcion: {valor_excepcion} - {tipo_excepcion} - {detalle_exepcion}')
        else:
            self._conexion.commit() #commit guarda los cambios si todo salio bien
            log.debug('Commit de la transaccion')
        self._cursor.close() # cerramos el objeto cursor
        Conexion.liberarConexion(self._conexion) # cerramos la conexion y la devolvemos al pool

#if __name__ == '__main__':
    #with CursorDelPool() as cursor:
        #log.debug('Dentro del bloque with')
        #cursor.execute('SELECT * FROM persona')
        #log.debug(cursor.fetchall()) #fetch recupera datos
