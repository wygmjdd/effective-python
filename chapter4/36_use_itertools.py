
import itertools


# 1. 将几个迭代器合成一个
it = itertools.chain([1, 2, 3], [4, 5, 6])
print('chain:', list(it))

# 2. 重复元素
#    注意：如果此处不传第2个参数生成的it直接转成list，是会把机器卡死的
it = itertools.repeat('hello', 3)

print(it)
for x in it:
    print(x)

# print('repeat:', list(it))


# 3. 一直循环下去，有点像是repeat
it = itertools.cycle([1, 2])
result = [next(it) for _ in range(9)]
print('cycle: ', result)


# 4. 复制n个出来
it1, it2, it3 = itertools.tee(['first', 'seconde'], 3)
print('tee 1:', list(it1))
print('tee 2:', list(it2))
print('tee 3:', list(it3))


# 5. zip，以长的为准
keys = ['one', 'two', 'three']
values = [1, 2]
normal = list(zip(keys, values))
print('zip normal:', normal)

it = itertools.zip_longest(keys, values, fillvalue='nope')
print('zip longest', list(it))


# 6. iter的切割
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
first_five = itertools.islice(values, 5)
print('islice first five:', list(first_five))

middle_odds = itertools.islice(values, 2, 8, 2)
print('islice middle odds:', list(middle_odds))


# 7. 按条件获取新的iter
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
less_than_seven = lambda x: x < 7  # NOQA
it = itertools.takewhile(less_than_seven, values)
print('takewhile: ', list(it))


# 8. 按条件筛掉某些部分
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
less_than_seven = lambda x: x < 7  # NOQA
it = itertools.dropwhile(less_than_seven, values)
print('dropwhile: ', list(it))
