import logging

class Log():
    def __init__(self, logfile = 'logfile.log'):
        self._logfile = logfile
        self._loglevel = logging.DEBUG
        self._logger = logging.getLogger('root')
        self._logger.setLevel(self._loglevel)
        self._fh = logging.FileHandler(self._logfile)
        self._fh.setFormatter('%(asctime)s %(filename)s:%(lineno)d %(levelname)s: %(message)s')
        self._logger.addHandler(self._fh)

    def critical(self, msg):
        self._logger.critical(msg)

    def debug(self, msg):
        self._logger.error(msg)

    def warn(self, msg):
        self._logger.warning(msg)

    def debug(self, msg):
        self._logger.debug(msg)

    def setLevel(self, loglevel):
        assert loglevel.upper in VALID_LOGLEVELS
        self._loglevel = loglevel
        self._logger.debug('Changing loglevel to {}'.format(loglevel))
        self._logger.setLevel(loglevel)