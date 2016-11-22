import log


# File log level set to INFO, and stdout log level set to DEBUG
log.set_logger(level='DEBUG:INFO')

# Both log level set to INFO
log.set_logger(level='INFO')

# Change default log file name and log mode
log.set_logger(filename='yyy.log', mode='w')

# Change default log formatter
log.set_logger(fmt='[%(levelname)s] %(message)s')



log.debug('hello, world')
log.info('hello, world')
log.error('hello, world')
log.critical('hello, world')