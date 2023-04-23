
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


# 9. 筛选函数
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = lambda x: x % 2 == 0  # NOQA
filter_result = filter(evens, values)
print('filter: ', list(filter_result))
filter_false_result = itertools.filterfalse(evens, values)
print('filter false:', list(filter_false_result))

# 10. 累加值
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_reduce = itertools.accumulate(values)
print('accumulate:', list(sum_reduce))


def sum_modulo_20(first, second):
    output = first + second
    return output % 20


modulo_reduce = itertools.accumulate(values, sum_modulo_20)
print('accumulate modulo:', list(modulo_reduce))


# 11. 计算笛卡尔积
single = itertools.product([1, 2, 3], repeat=2)
print('product single:', list(single))
multiple = itertools.product([1, 2], ['a', 'b', 'c'])
print('product multiple:', list(multiple))


# 12. 排列，并且是有序的
it = itertools.permutations([1, 2, 3, 4], 2)
print('permutations:', list(it))


# 13. 组合，也是有序的
it = itertools.combinations([1, 2, 3, 4], 2)
print('combinations:', list(it))


# 14. 多次出现的组合
it = itertools.combinations_with_replacement([1, 2, 3, 4], 2)
print('combinations_with_replacement:', list(it))
