

# 1. 返回list的版本，主要有两个问题
#    a、代码可读性没有迭代器好
#    b、如果返回list很大，但又不全用，会很浪费资源（内存、cpu）
def index_words(text):
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter == ' ':
            result.append(index + 1)
    return result


address = 'Four score and seven years ago...'
result = index_words(address)
print(result[:10])


# 2. 生成器版本
def index_words_iter(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1


it = index_words_iter(address)
print(next(it))
print(next(it))

# 如果想要获得跟上面一样结果，是可以直接list转的
result_it = list(it)
print(result_it[:10])
