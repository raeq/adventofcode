import functools
import logging

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


class logwith(object):
    '''Logging decorator that allows you to log with a
    specific logger.
    '''
    # Customize these messages
    ENTRY_MESSAGE = 'Entering {}'
    EXIT_MESSAGE = 'Exiting {}'

    def __init__(self, logger=None):
        self.logger = logger

    def __call__(self, func):
        '''Returns a wrapper that wraps func.
        The wrapper will log the entry and exit points of the function
        with logging.INFO level.
        '''
        # set logger if it was not set earlier
        if not self.logger:
            logging.basicConfig()
            self.logger = logging.getLogger(func.__module__)

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            self.logger.debug(f"Entry {func.__name__} args: {args}")
            f_result = func(*args, **kwargs)
            self.logger.debug(f"Leaving {func.__name__} with result '{f_result}'")
            return f_result

        return wrapper
