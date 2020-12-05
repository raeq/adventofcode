import logging
from functools import wraps
from time import process_time


def timing(wrapped, instance, args, kwargs):
    p1 = process_time()

    def _execute(*_args, **_kwargs):
        return wrapped(*_args, **_kwargs)

    p2 = process_time()
    print(f" {args} {kwargs} took {p2 - p1} s")

    return _execute(*args, **kwargs)


def invocation_log(func):
    @wraps(func)
    def inner_func(*args, **kwargs):
        log = logging.getLogger("aoc")
        log.debug(f'##entering:{func.__name__}, args:{args} kwargs: {kwargs}')
        retvalue = func(*args, **kwargs)
        log.debug(f'##leaving:{func.__name__}, returned: {retvalue}')
        return retvalue

    return inner_func
