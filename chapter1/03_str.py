

# 1. 打印hello
def test1():
    a = b'h\x65llo'
    print(list(a))
    print(a)


# 2. 打印一个特殊字符
def test2():
    a = 'a\u0300 propos'
    print(list(a))
    print(a)


# 3. bytes和str的互相转换
def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value  # Instance of str


def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value  # Instance of bytes


def test3():
    print(repr(to_str(b'foo')))
    print(repr(to_str('bar')))

    print(repr(to_bytes(b'foo')))
    print(repr(to_bytes('bar')))


# 4. 计算、比较和连接
def test4():
    # a. 同类相连
    print(b'one' + b'two')
    print('one' + 'two')

    # b. 异类报错
    print(b'one' + 'two')
    print('one' + b'two')

    # c. 同类可比
    print(b'red' > b'blue')
    print('red' > 'blue')

    # d. 异类报错
    print('red' > b'blue')
    print(b'blue' < 'red')

    # e. 两种不一样的对象
    print(b'foo' == 'foo')

    # f. 同类可拼接
    print(b'red %s' % b'blue')
    print('red %s' % 'blue')

    # g. str不能拼在bytes里面
    print(b'red %s' % 'blue')

    # h. bytes可以拼在str里
    tmp = 'red %s' % b'blue'
    print(tmp, type(tmp))


# 5. 读写文件
def test5():
    # a. 写数据必须得是写str，因为open参数默认是str
    with open('data.bin', 'w') as f:
        f.write(b'\xf1\xf2\xf3\xf4\xf5')

    # b. 可写bytes
    with open('data.bin', 'wb') as f:
        f.write(b'\xf1\xf2\xf3\xf4\xf5')

    # c. 读文件默认为str，此文件不能被解析
    with open('data.bin', 'r') as f:
        _ = f.read()

    # d. 以二进制格式读文件
    with open('data.bin', 'rb') as f:
        data = f.read()
        print(data == b'\xf1\xf2\xf3\xf4\xf5')

    # f. 以cp1252字符集对bytes进行编码
    with open('data.bin', 'r', encoding='cp1252') as f:
        data = f.read()
        print(data == 'ñòóôõ')


if __name__ == '__main__':
    # test1()
    # test2()
    # test3()
    # test4()
    test5()
