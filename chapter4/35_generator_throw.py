

class MyError(Exception):
    pass


def my_generator():
    yield 1
    yield 2
    yield 3


it = my_generator()
print(next(it))
print(next(it))
print(it.throw(MyError('test error')))
