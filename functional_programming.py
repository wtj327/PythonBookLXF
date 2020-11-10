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
    values_new = map(func, values)  # map returns an iterator
    print(list(values))
    print(list(values_new))  # convert the iter to a list
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
            dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '.': 0}
            return dict[char]

        # separate int and float in s
        s_int = s[:s.index('.'):]
        s_float = s[s.index('.')::]
        # convert str to separate digits(int)
        digits_int = list(map(char_to_digit, s_int))
        digits_float = list(map(char_to_digit, s_float))

        # define 2 func that converts separate digits to a num (int or pure float)
        def digits_to_int(x, y):
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

    # Use of filter()
    def is_even(num):
        return num % 2 == 0

    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list2 = list(filter(is_even, list1))  # filter() returns a iterator
    print(list2)
    print()

    # Use of filter, Example 2
    # 把一个序列中的空字符串删掉
    def not_empty(s):
        return s and s.strip()

    list1 = ['A', '', 'B', None, 'C', '  ']
    list2 = list(filter(not_empty, list1))
    print(list1)
    print(list2)
    print()

    # Use of filter, Example 3：用filter求素数
    # Define a odd number generator, staring with 3
    def odd_num_gen():
        n = 1
        while True:
            n = n + 2
            yield n

    # Define a filter function
    def not_divisible(n):
        return lambda x: x % n > 0

    # Create the prime number generator
    def prime_num_gen():
        yield 2
        numbers = odd_num_gen()
        while True:
            n = next(numbers)  # get the first num in the queue
            yield n
            numbers = filter(not_divisible(n), numbers)  # update the queue

    # generator all prime numbers within a threshold
    for n in prime_num_gen():
        if n < 100:
            print(n)
        else:
            break
    print()

    # Use of filter, Quiz: 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：
    # define a filter
    def is_palindrome(n):
        return str(n) == str(n)[::-1]

    # 测试:
    output = filter(is_palindrome, range(1, 1000))
    print('1~1000:', list(output))
    if list(filter(is_palindrome, range(1, 200))) == \
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, \
             101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
        print('测试成功!')
    else:
        print('测试失败!')
    print()

    # sorted() function
    list1 = [36, 5, -12, 9, -21]
    list2 = sorted(list1)
    print(list1)
    print(list2)
    list3 = sorted(list1, key=abs)
    print(list3)
    list1 = ['bob', 'about', 'Zoo', 'Credit']
    list2 = sorted(list1)
    print(list1)
    print(list2)
    list3 = sorted(list1, key=str.lower)
    print(list3)
    list4 = sorted(list1, key=str.lower, reverse=True)
    print(list4)
    print()
    # sorted(), quiz:
    # 假设我们用一组tuple表示学生名字和成绩
    L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

    # 请用sorted()对上述列表分别按名字排序
    def by_name(t):
        return str.lower(t[0])

    L2 = sorted(L, key=by_name)
    print(L2)
    print()

    # 再按成绩从高到低排序
    def by_score(t):
        return -t[1]

    L2 = sorted(L, key=by_score)
    print(L2)
    print()

    # Closure 闭包，返回函数
    # Quiz: 利用闭包返回一个计数器函数，每次调用它返回递增整数
    def createCounter():
        count = [0]  # must use a changeable object

        def counter():
            count[0] += 1
            return count[0]

        return counter

    # 测试:
    counterA = createCounter()
    print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
    counterB = createCounter()
    if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
        print('测试通过!')
    else:
        print('测试失败!')
    print()

    # 匿名函数
    # 关键字lambda表示匿名函数，冒号前面的x表示函数参数。
    # 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
    # 用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。此外，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，
    # 再利用变量来调用该函数
    list1 = [1, 2, 3, 4, 5]
    print(list(map(lambda x: x * x, list1)))
    foo = lambda x: x * x
    print(list(map(foo, list1)))
    print()

    # 也可以把匿名函数作为返回值返回
    def foo(x, y):
        return lambda: x ** 2 + y ** 2
    foo1 = foo(1, 2)
    print(foo1)
    print(foo1())
    print()

    # 匿名函数，Quiz
    L = list(filter(lambda x: x%2 == 1, range(1, 20)))
    print(L)
    print()

    # Decorator 装饰器
    import functools
    def log(text):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print('%s %s():' % (text, func.__name__))
                return func(*args, **kw)
            return wrapper
        return decorator

    @log('execute')
    def now():
        print('2020-11-07')

    now()
    print(now.__name__)
    print()
    # decorator, quiz: 请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间
    import time
    def metric(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kw):
            t0 = time.time()
            result = fn(*args, **kw)
            t1 = time.time()
            print('%s executed in %s ms' % (fn.__name__, t1-t0))
            return result
        return wrapper
    # test decorator
    @metric
    def fast(x, y):
        time.sleep(0.0012)
        return x + y;
    @metric
    def slow(x, y, z):
        time.sleep(0.1234)
        return x * y * z;

    f = fast(11, 22)
    s = slow(11, 22, 33)
    if f != 33:
        print('测试失败!')
    elif s != 7986:
        print('测试失败!')
    print()

    # 偏函数 Partial Function
    int1 = int('100')
    print(int1)
    int2 = int('100', base=2)
    print(int2)
    import functools
    int2 = functools.partial(int, base=2)
    int3 = int2('100')
    print(int3)
    dict_ = {'base': 2}
    int_based_2 = functools.partial(int, **dict_)
    int4 = int_based_2('100')
    print(int4)
    print()

    # 测试：对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的
    def hello(name):
        print('Hello, %s' % name)
    hello('Tom')
    list_ = ['Taylor']
    dict_ = {}
    hello(*list_, **dict_)

    print('End of functional programming')
    print()

















