
from collections.abc import Iterator


NUMS_LENGTH = 3


# 0. 返回生成器的函数, 可能数据量超级大
def my_read_visit():
    for i in range(NUMS_LENGTH):
        yield i


# 1. 最初的版本
def normalize(numbers):
    total = sum(numbers)
    result = []
    # Already exhausted, generator只能转成list一次
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


nums = my_read_visit()
print('is Iterator: ', isinstance(nums, Iterator))
print('is Iterator2: ', iter(nums) is nums)
print('normalize(nums): ', normalize(nums))


# 2. 计算前先拷贝一把生成器中的内容
#    弊端：本来使用生成器就是为了省内存，拷贝则又出现内存多用情况了
def normalize_copy(numbers):
    numbers_copy = list(numbers)  # Copy the iterator
    total = sum(numbers_copy)
    result = []
    for value in numbers_copy:
        percent = 100 * value / total
        result.append(percent)
    return result


nums = my_read_visit()
print('normalize_copy(nums): ', normalize_copy(nums))


# 3. 下一个优化版本，直接传递能够生成生成器的函数
#    弊端：传一个生成器函数，代码可读性上有点怪怪的
def normalize_func(get_iter):
    total = sum(get_iter())   # New iterator
    result = []
    for value in get_iter():  # New iterator
        percent = 100 * value / total
        result.append(percent)
    return result


print('normalize_func(my_read_visit): ', normalize_func(my_read_visit))


# 4. 传递一个对象，这个对象在真正使用时产生一个生成器
class MyReadVisits:
    def __init__(self, *args):
        self.args = args  # 书中参数有用到，我这里略过了

    def __iter__(self):
        for i in range(NUMS_LENGTH):
            yield i


print('normalize give one object: ', normalize(MyReadVisits()))
