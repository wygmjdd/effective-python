
# 1. 普通的格式化，用符号%和tuple
def test1():
    a = 0b10111011
    b = 0xc5f
    print('Binary is %d, hex is %d' % (a, b))


# 2. 格式化
def test2():
    key = 'my_var'
    value = 1.234
    # 加空格到10个字符宽度，浮点数只展示2位小数
    formatted = '%-10s = %.2f' % (key, value)
    print('formatted', formatted)

    # %f需要与浮点数配对
    reordered_tuple = '%-10s = %.2f' % (key, value)
    print('reordered_tuple', reordered_tuple)


# 3. %符号格式化的不太好的地方
def test3():
    pantry = [
        ('avocados', 1.25),
        ('bananas', 2.5),
        ('cherries', 15),
    ]
    # a. 打印数据
    for i, (item, count) in enumerate(pantry):
        print('#%d: %-10s = %.2f' % (i, item, count))

    # b. 打印太长，将代码换行，丧失部分可读性
    #    （这里的示例，其实放在一行内是完全可以的，少于79个字符）
    for i, (item, count) in enumerate(pantry):
        print('#%d: %-10s = %d' % (
            i + 1,
            item.title(),
            round(count)))

    # c. 相同的值，会需要在右边写多次
    template = '%s loves food. See %s cook.'
    name = 'Max'
    formatted = template % (name, name)
    print(formatted)


if __name__ == '__main__':
    # test1()
    # test2()
    test3()
