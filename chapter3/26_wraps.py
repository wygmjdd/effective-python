from functools import wraps


def trace(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'{func.__name__}({args!r}, {kwargs!r}) '
              f'-> {result!r}')
        return result
    return wrapper


@trace
def f(n):
    ''' return the n-th f number'''
    if n in (0, 1):
        return n
    return f(n - 2) + f(n - 1)
