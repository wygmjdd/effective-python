
import math


# 1. 初始版本
def wave(amplitude, steps):
    step_size = 2 * math.pi / steps
    for step in range(steps):
        radians = step * step_size
        fraction = math.sin(radians)
        output = amplitude * fraction
        yield output


def transmit(output):
    if output is None:
        print('Output is None')
    else:
        print(f'Output: {output:>5.1f}')


def run(it):
    for output in it:
        transmit(output)


# 2. send初使用
def my_generator():
    '''
    Using yield on the right side of an assignment statement
    isn’t intuitive, and it’s hard to see the connection between yield and
    send without already knowing the details of this advanced generator
    feature.
    赋值语句的右边放一个yield接收输入，很不直观!
    '''
    received = yield 1
    print(f'  > received = {received}')


def test_without_send():
    print('test_without_send:')
    it = my_generator()
    output = next(it)
    print(f'  > output = {output}')
    try:
        next(it)
    except StopIteration:
        print('  > iter stopped')


def test_with_send():
    print('test_with_send:')
    it = my_generator()
    # send的第一个值必须是None
    output = it.send(None)
    print(f'  > output = {output}')
    try:
        it.send('hello!')
    except StopIteration:
        print('  > iter stopped')


# 3. 改造版的wave
def wave_modulating(steps):
    step_size = 2 * math.pi / steps
    amplitude = yield  # 接收初始 amplitude，停下来，并返回None，等待下次调用
    for step in range(steps):
        radians = step * step_size
        fraction = math.sin(radians)
        output = amplitude * fraction
        # 接收下一个 amplitude
        # 这里其实是先接受了amplitude的值，然后再将output返回出去
        amplitude = yield output


def run_modulating(it):
    amplitudes = [None, 7, 6, 5, 2, 2, 2, 2, 10, 10, 10, 10, 10]
    for _, amplitude in enumerate(amplitudes):
        output = it.send(amplitude)
        transmit(output)


# 4. 需求升级，wave变复杂了
def complex_wave():
    yield from wave(7.0, 3)
    yield from wave(2.0, 4)
    yield from wave(10.0, 5)


def complex_wave_modulating():
    # 这个版本有很多的None输出
    yield from wave_modulating(3)
    yield from wave_modulating(4)
    yield from wave_modulating(5)


# 5. 最终版本
#    去掉send的使用，直接传递一个生成器进来
def wave_cascading(amplitude_it, steps):
    step_size = 2 * math.pi / steps
    for step in range(steps):
        radians = step * step_size
        fraction = math.sin(radians)
        amplitude = next(amplitude_it)  # 获取下一个输入
        output = amplitude * fraction
        yield output


def complex_wave_cascading(amplitude_it):
    yield from wave_cascading(amplitude_it, 3)
    yield from wave_cascading(amplitude_it, 4)
    yield from wave_cascading(amplitude_it, 5)


def run_cascading():
    amplitudes = [7, 7, 7, 2, 2, 2, 2, 10, 10, 10, 10, 10]
    it = complex_wave_cascading(iter(amplitudes))
    for amplitude in amplitudes:
        output = next(it)
        transmit(output)


if __name__ == '__main__':
    # run(wave(3.0, 8))
    # run_modulating(wave_modulating(12))
    # run(complex_wave())
    # run_modulating(complex_wave_modulating())
    run_cascading()

    # test_without_send()
    # test_with_send()
