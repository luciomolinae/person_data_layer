import logging as log

#log = logging

#log.basicConfig(level=log.INFO) = level=log.WARNING

log.basicConfig(level=log.DEBUG,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s', #asctime esto agrega el tiempo (fecha y hora) al mensaje del log levelname esto agrega si fue debug, info, etc filename esto agrega el nombre del archivo del mensaje del log lineno agrega la linea que lanzo el error message esto muestra el mensaje que hemos agregado al log
                datefmt='%I:%M:%S %p',
                handlers= [             #agregamos informacion a un archivo, en este caso una lista
                    log.FileHandler('capa_datos.log'),
                    log.StreamHandler()
                ])

#if __name__ == '__main__':
    #log.debug('Mensaje a nivel debug')
    #log.info('Mensaje a nivel info')
    #log.warning('Mensaje a nivel de warning')
    #log.error('Mensaje a nivel de error')
    #log.critical('Mensaje a nivel de critico')
