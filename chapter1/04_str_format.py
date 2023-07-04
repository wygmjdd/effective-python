
pantry = [
    ('avocados', 1.25),
    ('bananas', 2.5),
    ('cherries', 15),
]


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


# 4. 新的格式化写法
def test4():
    key = 'my_var'
    value = 1.234

    # a. 旧的写法
    old_way = '%-10s = %.2f' % (key, value)
    print(f'old_way0: {old_way}')

    # b1. 新的写法
    new_way = '%(key)-10s = %(value).2f' % {
        'key': key, 'value': value
    }
    # b2. dict中的顺序并不影响
    reordered = '%(key)-10s = %(value).2f' % {
        'value': value, 'key': key
    }
    print(f'new_way1: {new_way}')
    print(f'new_way2: {reordered}')

    # c. 上面的重复内容，不用写两次啦
    name = 'Max'
    template = '%s loves food. See %s cook.'
    before = template % (name, name)  # Tuple
    template = '%(name)s loves food. See %(name)s cook.'
    after = template % {'name': name}  # Dictionary
    print(f'before: {before}')
    print(f'after : {after}')

    # d1. 这种写法，也不太好，变量名要敲两次，就是敲的字符数变多了
    for i, (item, count) in enumerate(pantry):
        before = '#%d: %-10s = %d' % (
            i + 1,
            item.title(),
            round(count)
        )

        after = '#%(loop)d: %(item)-10s = %(count)d' % {
            'loop': i + 1,
            'item': item.title(),
            'count': round(count),
        }

        print(f'before: {before}')
        print(f'after : {after}')

    # d2. 再者，如果字符串很长需要分行的话，也不好看
    menu = {
        'soup': 'lentil',
        'oyster': 'kumamoto',
        'special': 'schnitzel'
    }
    template = ('Today\'s soup is %(soup)s, '
                'buy one get two %(oyster)s oysters, '
                'and our special entrée is %(special)s.')
    formatted = template % menu
    print(formatted)


# 5. 更好的办法
def test5():
    pass


if __name__ == '__main__':
    # test1()
    # test2()
    # test3()
    test4()
