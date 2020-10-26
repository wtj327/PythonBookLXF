#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Python Advanced Features

def test_code():
    # slice
    names = ['Tianjiao', 'Tao', 'Taylor']
    names_2 = names[0:2]
    print(names_2)
    # slice 2
    my_list = list(range(1,21))
    print(my_list)
    print(my_list[0:10:2])
    print(my_list[-10:-1:2])
    print(my_list[::5])
    # slice tuple, get tuple
    my_tuple = tuple(range(1,11))
    print(my_tuple)
    print(my_tuple[0:5:2])
    # slice str, get str
    my_str = 'hello world'
    print(my_str)
    print(my_str[0:6:2])
    print()

    # Quiz: 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法
    def trim(s):
        while s[0:1:] == ' ':
            s = s[1::]
        while s[-1::] == ' ':
            s = s[:-1:]
        return s
    # Test quiz
    if trim('hello  ') != 'hello':
        print('测试失败!')
    elif trim('  hello') != 'hello':
        print('测试失败!')
    elif trim('  hello  ') != 'hello':
        print('测试失败!')
    elif trim('  hello  world  ') != 'hello  world':
        print('测试失败!')
    elif trim('') != '':
        print('测试失败!')
    elif trim('    ') != '':
        print('测试失败!')
    else:
        print('测试成功!')
    print()

    # iteration (迭代)：如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）
    # list iteration
    my_list = list(range(1,11))
    print(my_list)
    is_first = True
    for item in my_list:
        if is_first:
            is_first = False
        else:
            print(', ', end='')
        print(item+1, end='')
    print()
    # tuple iteration
    my_tuple = tuple(range(1,11))
    print(my_tuple)
    is_first = True
    for item in my_tuple:
        if is_first:
            is_first = False
        else:
            print(', ', end='')
        print(item+2, end='')
    print()
    # dictionary iteration 1
    my_dict = {'Tianjiao': 37, 'Tao': 35, 'Taylor': 1}
    print(my_dict)
    is_first = True
    for key in my_dict:
        if is_first:
            is_first = False
        else:
            print(', ', end='')
        print(key, end='')
    print()
    # dictionary iteration 2
    is_first = True
    for value in my_dict.values():
        if is_first:
            is_first = False
        else:
            print(', ', end='')
        print(value, end='')
    print()
    # dictionary iteration 3
    is_first = True
    for key, value in my_dict.items():
        if is_first:
            is_first = False
        else:
            print(', ', end='')
        print(key, value, end='')
    print()
    # string iteration
    my_str = 'Tianjiao'
    for e in my_str:
        print(e)
    print()

    # 如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断
    from collections import Iterable
    print(isinstance(my_list, Iterable))
    print(isinstance(my_tuple, Iterable))
    print(isinstance(my_dict, Iterable))
    print(isinstance(my_str, Iterable))
    print(isinstance(123, Iterable))
    print()

    # 如果要对list实现类似Java那样的下标循环怎么办？
    # Python内置的enumerate函数可以把一个list变成索引 - 元素对，这样就可以在for循环中同时迭代索引和元素本身
    print(my_list)
    for index, elmt in enumerate(my_list):
        print(index, elmt)
    print()

    # quiz: 请使用迭代查找一个list中最小和最大值，并返回一个tuple：
    def findMinAndMax(L):
        if len(L) == 0:
            return None, None
        else:
            min = L[0]
            max = L[0]
            for value in L:
                if value < min:
                    min = value
                if value > max:
                    max = value
            return min, max
    # test quiz:
    if findMinAndMax([]) != (None, None):
        print('测试失败!')
    elif findMinAndMax([7]) != (7, 7):
        print('测试失败!')
    elif findMinAndMax([7, 1]) != (1, 7):
        print('测试失败!')
    elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
        print('测试失败!')
    else:
        print('测试成功!')
    print()

    # 列表生成式
    # Basic
    my_list = list(range(1,11))
    print(my_list)
    # Adv
    my_list = list(v*v for v in my_list)
    print(my_list)
    # Adv
    my_list = list(v*v for v in my_list if v%2==0)
    print(my_list)
    # Adv, full permutations
    list_1 = ['A', 'B', 'C']
    list_2 = ['1', '2', '3']
    list_3 = list(v1+v2 for v1 in list_1 for v2 in list_2)
    print(list_3)
    # 运用列表生成式，可以写出非常简洁的代码。例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现
    import os
    print(list(v for v in os.listdir('.')))
    print()
    # 把一个list中所有的字符串变成小写
    list1 = ['Tianjiao', 'Tao', 'TAYLOR']
    list2 = list(v.lower() for v in list1)
    print(list2)
    # 在一个列表生成式中，for前面的if ... else是表达式，而for后面的if是过滤条件，不能带else
    list1 = [v if v>=0 else -v for v in range(-10, 11)]
    print(list1)
    print()
    # quiz: modify tolower method
    L1 = ['Hello', 'World', 18, 'Apple', None]
    L2 = [v.lower() for v in L1 if isinstance(v, str)]
    # test quiz
    print(L2)
    if L2 == ['hello', 'world', 'apple']:
        print('测试通过!')
    else:
        print('测试失败!')
    print()

    # 生成器 generator





























