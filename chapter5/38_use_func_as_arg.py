

# 1. 按字符串长度排序
def test1():
    names = ['Socrates', 'Archimedes', 'Plato', 'Aristotle']
    names.sort(key=len)
    print(names)


if __name__ == '__main__':
    test1()
