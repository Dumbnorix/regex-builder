import functools
import logging

logging.basicConfig(
            format='%(asctime)s %(message)s',
            level=logging.DEBUG,
            datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger('traceLogger')

def Log(skip=False, quiet=False):
    def Trace(f):
        def wrapper(*args, **kwargs):
            value = f(*args, **kwargs)
            if skip == True:
                return value
            if quiet == True:
                logger.debug(' --- FUNCTION %s', f.__name__)
                logger.debug(' --- RETURNED')
            else:
                logger.debug(' --- FUNCTION %s%s', f.__name__, args[1:])
                logger.debug(' --- RETURNED: %s', value)
            return value
        return wrapper
    return Trace