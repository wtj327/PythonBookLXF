#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# test some inner functions
var_test = -100
var_test_2 = abs(var_test)
print(var_test)
print(var_test_2)
print(max(0, 1, 2, 100, 99))
print(min(0, 1, 2, 100, 99))
# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：
test_func = abs
print(test_func(-50))
var_test = 16
var_test_2 = hex(var_test)
print(var_test_2)
print()

# define a new function
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

# call the defined func
var_test = -123
print(my_abs(var_test))
print()
# 定义默认参数要牢记一点：默认参数必须指向不变对象！

# 可变参数
# 给定一组数字a，b，c……，请计算a2 + b2 + c2 + ……
# *nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。
def cal_sum_square(*nums):
    sum = 0
    for num in nums:
        sum += num ** 2
    return sum
print(cal_sum_square(1,2,3))
print(cal_sum_square(1,2))
my_list = [1,2,3]
print(cal_sum_square(*my_list))
my_tuple = (1,2,3)
print(cal_sum_square(*my_tuple))
print()

# 函数的几个参数的概念：位置参数，默认参数，可变参数，关键字参数
def my_func(name, age, **kw):
    print(name, age, kw)
my_func('Tom', '37')
my_dict = {'sex': 'male', 'Nationality': 'China'}
my_func('Tom', '37', **my_dict)
my_func('Tom', '37', Sex='male', Nationality='China')
print()

# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
# 默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误
# 使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法
# 对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的
# Practice:
def product(*nums):
    product = 1
    for num in nums:
        product = product * num
    return product
print(product(1,2,3,4,5))
nums = (1,2,3,4,5)
print(product(*nums))
nums = [1,2,3,4,5]
print(product(*nums))
print(product())
print()

# 递归函数
# 典型例子，汉诺塔
# n is the number of circles in the ori at the beginning of the problem
# ori is the name of the origin tower at the beginning of the problem
# dest is the name of the destination tower at the beginning of the problem
# mid it the name of the middle tower at the beginning of the problem
def solve_hanoi(n, ori, mid, dest):
    if n==1:
        print(ori, '-->', dest)
    else:
        solve_hanoi(n-1, ori, dest, mid)
        print(ori, '-->', dest)
        solve_hanoi(n-1, mid, ori, dest)
# call the function
print(' n = 1:')
solve_hanoi(1, 'A', 'B', 'C')
print()
print('n = 2:')
solve_hanoi(2, 'A', 'B', 'C')
print()
print('n = 3:')
solve_hanoi(3, 'A', 'B', 'C')
























