
stock = {
    'nails': 125,
    'screws': 35,
    'wingnuts': 8,
    'washers': 24,
}


order = ['screws', 'wingnuts', 'clips']


def get_batches(count, size):
    return count // size


result1 = {}
# 1. 原始版本
for name in order:
    count = stock.get(name, 0)
    batches = get_batches(count, 8)
    if batches:
        result1[name] = batches

# 2. 使用推导式版本，有重复代码
result2 = {
    name: get_batches(stock.get(name, 0), 8)
    for name in order
    if get_batches(stock.get(name, 0), 8)
}

# 3. 使用海象版本，更清晰
result3 = {
    name: batches
    for name in order if (batches := get_batches(stock.get(name, 0), 8))
}


print('result1', result1)
print('result2', result2)
print('result3', result3)

# 1. last会溢出
half = [(last := count1 // 2) for count1 in stock.values()]
print(f'Last item of {half} is {last}')

# 2. count2会溢出
for count2 in stock.values():  # Leaks loop variable
    pass
print(f'Last item of {list(stock.values())} is {count2}')

# 3. count3不会溢出，print(count3)会报错
half = [count3 // 2 for count3 in stock.values()]
print(half)   # Works
print(count3)  # Exception because loop variable didn't leak
