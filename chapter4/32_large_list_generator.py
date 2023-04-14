
import numpy
import os
import psutil


FILE_NAME = 'tmp_my_file.txt'


def write_file():
    with open(FILE_NAME, 'w') as file:
        value = [
            numpy.random.rand(10).tolist()
            for _ in range(1000000)
        ]
        file.write('\n'.join(map(str, value)))


def read_file_by_list():
    file = open(FILE_NAME)
    value = [len(x) for x in file]
    print(len(value))
    return file


def read_file_by_it():
    file = open(FILE_NAME)
    it = (len(x) for x in file)
    print('it', it)
    print('next(it)', next(it))

    # 生成器嵌套
    # (203, 14.247806848775006)
    roots = ((x, x ** 0.5) for x in it)
    print(next(roots))

    return file


if __name__ == '__main__':
    process = psutil.Process(os.getpid())
    init_size = process.memory_info().rss / 1024
    print(f'打开文件之前占用内存： {init_size} KB')

    # 1. 先写一个文件，文件大小是19M
    # write_file()

    # 2.1 结果存在生成器中
    file = read_file_by_it()
    # 2.2 结果存在list中
    # file = read_file_by_list()

    # 获取当前进程的内存占用情况
    end_size = process.memory_info().rss / 1024
    print(f'打开文件之后占用内容： {end_size} KB, 差异值为：{end_size - init_size} KB')

    print(file.fileno())
