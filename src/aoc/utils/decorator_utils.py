from functools import wraps

from time import process_time


def timing(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        p1 = process_time()
        result = f(*args, **kwargs)
        p2 = process_time()
        print(f"func:{f.__name__} with {args} {kwargs} took {p2 - p1} s")
        return result

    return wrap
