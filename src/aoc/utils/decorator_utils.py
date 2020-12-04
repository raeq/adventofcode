from time import process_time


def timing(wrapped, instance, args, kwargs):
    p1 = process_time()

    def _execute(*_args, **_kwargs):
        return wrapped(*_args, **_kwargs)

    p2 = process_time()
    print(f" {args} {kwargs} took {p2 - p1} s")

    return _execute(*args, **kwargs)
