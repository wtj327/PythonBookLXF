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
    # 要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator
    my_list = [v ** 2 for v in range(1,11)]
    print(my_list)
    # generator, which stores 'the algorithm'
    g = (v ** 2 for v in range(1,11))
    print(next(g))
    # generator也是可迭代对象
    for v in g:
        print(v)
    print()

    # Create a generator
    def fib(max):
        n, a, b = 0, 0, 1
        while n < max:
            yield b
            a, b = b, a + b
            n = n + 1
        return 'done'
    # Call the generator
    g = fib(5)
    print(next(g))
    print(next(g))
    print()
    # 把函数改成generator后，我们基本上从来不会用next()来获取下一个返回值，而是直接使用for循环来迭代
    for v in g:
        print(v)
    print()
    # Use a generator to build Pascal's Triangle
    def triangles():
        row = [1]
        while True:
            yield row
            row_temp = [0] + row
            row = row + [0]
            row_new = []
            for x, y in zip(row_temp, row):
                row_new.append(x+y)
            row = row_new
    # Call
    f = triangles()
    print(next(f))
    print(next(f))
    print(next(f))
    print(next(f))
    print(next(f))
    # Test
    n = 0
    results = []
    for t in triangles():
        results.append(t)
        n = n + 1
        if n == 10:
            break

    for t in results:
        print(t)

    if results == [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1],
        [1, 5, 10, 10, 5, 1],
        [1, 6, 15, 20, 15, 6, 1],
        [1, 7, 21, 35, 35, 21, 7, 1],
        [1, 8, 28, 56, 70, 56, 28, 8, 1],
        [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
    ]:
        print('测试通过!')
    else:
        print('测试失败!')
    print()

    # Summary: 可以直接作用于for循环的数据类型有以下几种：
    # 一类是集合数据类型，如list、tuple、dict、set、str等；
    # 一类是generator，包括生成器和带yield的generator function
    # 这些可以直接作用于for循环的对象统称为可迭代对象：Iterable
    # 可以使用isinstance()判断一个对象是否是Iterable对象
    from collections.abc import Iterable
    print(isinstance([1,2,3], Iterable))
    print(isinstance((v for v in range(1,10)), Iterable))
    print()

    # 迭代器，Iterator: 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
    # 可以使用isinstance()判断一个对象是否是Iterator对象
    from collections.abc import Iterator
    print(isinstance([1,2,3], Iterator))
    print(isinstance((v for v in range(1,10)), Iterator))
    print()

    # 生成器Generator都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
    # 把list、dict、str等Iterable变成Iterator可以使用iter()函数
    print(isinstance([1,2,3], Iterator))
    print(isinstance(iter([1,2,3]), Iterator))
    f = iter([1,2,3])
    print(next(f))
    print(next(f))
    print(next(f))
    print()
    # Convert iterator to list
    f = iter([1, 2, 3, 4, 5])
    print(f)
    print(next(f))
    print(list(f))
    print()

    ''' 你可能会问，为什么list、dict、str等数据类型不是Iterator？
    这是因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，
    直到没有数据时抛出StopIteration错误。
    可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，
    所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。
    Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。
    REF: https: // www.liaoxuefeng.com / wiki / 1016959663602400 / 1017323698112640 '''










