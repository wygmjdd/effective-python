
import time


class MyError(Exception):
    pass


# 1. throw的使用
def generator1():
    yield 1
    yield 2
    yield 3


def throw(it):
    print('1' * 30, next(it))
    print('2' * 30, it.throw(MyError('test error')))
    print('3' * 30, next(it))


def test1():
    it = generator1()
    try:
        # 不抓异常的话，会直接从这里退出进程
        throw(it)
    except Exception as e:
        print('exception: ', e)

    print('after throw', it)
    next(it)


# 2. 在生成器里面抓异常
def generator2():
    yield 1

    try:
        yield 2
    except MyError:
        print('Got MyError!')
    else:
        yield 3

    yield 4


def test2():
    it = generator2()
    print('1' * 30, next(it))
    print('2' * 30, next(it))
    print(it.throw(MyError('test error')))
    # print('3' * 30, next(it))
    # print('4' * 30, next(it))
    # print('5' * 30, next(it))


# 3. 重置计时器
class Reset(Exception):
    pass


def check_for_reset():
    # change_val = int(time.time() * 1000)
    change_val = time.monotonic_ns()
    return change_val % 2 == 0


def announce(remaining):
    print(f'{remaining} ticks remaining')


def timer(period):
    current = period
    while current:
        current -= 1
        try:
            yield current
        except Reset:
            current = period


def test3():
    it = timer(4)
    while True:
        try:
            if check_for_reset():
                current = it.throw(Reset())
            else:
                current = next(it)
        except StopIteration:
            break
        else:
            announce(current)


# 4. test3可读性不高，再换成类
class Timer:
    def __init__(self, period):
        self.current = period
        self.period = period

    def reset(self):
        self.current = self.period

    def __iter__(self):
        while self.current:
            self.current -= 1
            yield self.current


def test4():
    timer = Timer(4)
    for current in timer:
        if check_for_reset():
            timer.reset()
        announce(current)


if __name__ == '__main__':
    # test1()
    # test2()
    # test3()
    test4()
