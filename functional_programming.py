#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Functional Programming

def test_code():
    print('##### Chapter: Functional Programming #####')
    # Test higher order functions
    # 编写高阶函数，就是让函数的参数能够接收别的函数
    def sum_func(x, y, f):
        return f(x) + f(y)
    print(sum_func(-1, 2, abs))
    print()

    # Test map(), Example 1
    def func(x):
        return x ** 2
    values = [1, 2, 3, 4, 5]
    values_new = map(func, values)    # map returns an iterator
    print(list(values))
    print(list(values_new))    # convert the iter to a list
    print()
    # Test map(), Example 2
    print(list(map(str, values)))
    print()
    # test reduce, Example 1: 把序列 [1, 3, 5, 7, 9] 变换成整数13579
    values = [1, 3, 5, 7, 9]
    def f1(x, y):
        return x * 10 + y
    from functools import reduce
    value_new = reduce(f1, values)
    print(value_new)
    print()
    # test map(), Practice: 把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字
    def normalize(name):
        name_normalized = name[0].upper() + name[1::].lower()
        return name_normalized
    # test
    L1 = ['adam', 'LISA', 'barT']
    L2 = list(map(normalize, L1))
    print(L2)
    print()
    # test reduce(), Quiz: Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积
    def prod(L):
        def multiply(x, y):
            return x * y
        return reduce(multiply, L)
    # test:
    print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
    if prod([3, 5, 7, 9]) == 945:
        print('测试成功!')
    else:
        print('测试失败!')
    print()
    # test map() and reduce(), Quiz: 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
    def str2float(s):
        def char_to_digit(char):
            dict = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '.':0}
            return dict[char]
        # separate int and float in s
        s_int = s[:s.index('.'):]
        s_float = s[s.index('.')::]
        # convert str to separate digits(int)
        digits_int = list(map(char_to_digit, s_int))
        digits_float = list(map(char_to_digit, s_float))
        # define 2 func that converts separate digits to a num (int or pure float)
        def digits_to_int (x, y):
            return x * 10 + y
        def digits_to_pure_float(x, y):
            return x * 0.1 + y
        # combine the final result
        result_int = reduce(digits_to_int, digits_int)
        result_float = reduce(digits_to_pure_float, digits_float[::-1])
        return result_int + result_float
    # Test
    print('str2float(\'123.456\') =', str2float('123.456'))
    if abs(str2float('123.456') - 123.456) < 0.00001:
        print('str2float 测试成功!')
    else:
        print('str2float 测试失败!')
    print(str2float('4567996.33'))
    print()
































