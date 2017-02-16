import time as _time
import functools as _functools

def timeme(fn):
    """the timeme decorator that prints the running time of a function."""

    @_functools.wraps(fn)
    def _fn(*args, **kwargs):
        start = _time.time()
        result = fn(*args, **kwargs)
        end = _time.time()

        print('%r (%r, %r) %2.2f sec' % (fn.__name__, args, kwargs, end-start))
        return result

    return _fn
