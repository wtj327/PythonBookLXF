# 当Python解释器读取源代码时，为了让它按UTF-8编码读取，我们通常在文件开头写上这两行：
# 第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
# 第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。
# 申明了UTF-8编码并不意味着你的.py文件就是UTF-8编码的，必须并且要确保文本编辑器正在使用UTF-8 without BOM编码
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def test_code():
    # Test input and output
    user_name = 'Tom'
    # user_name = input('Please input your full name: ')
    print('Hello,', user_name)
    # Test output multiple lines
    print('''Line 1
    %s
    %s
    Line 3''' %(user_name, user_name))
    # Test r operation
    print(r'''hello,\n
    world''')
    print()

    # 空值是Python里一个特殊的值，用None表示。None不能理解为0，因为0是有意义的，而None是一个特殊的空值。

    # Test variables
    a = 'ABC'
    b = a
    a = 'XYZ'
    print(b)
    print()

    # Test UTF-8 encoding and decoding
    print('早上好')
    print()

    # len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数：
    print(len('测试'))
    test_encode = '测试'.encode('utf-8')
    print(test_encode)
    print(len(test_encode))
    print()

    # 格式化整数和浮点数还可以指定是否补0和整数与小数的位数
    print('%.2f, %2.3f' %(3.1415926, 3.1415926))
    print('%2d, %02d' % (3, 1))
    # 有些时候，字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%：
    print('The probability is %.2f%%' %(75.12345))
    # 另一种格式化字符串的方法是使用字符串的format()方法，它会用传入的参数依次替换字符串内的占位符{0}、{1}……，不过这种方式写起来比%要麻烦得多：
    print('The probability of {0} is {1:.2f}%'.format('Event A', 75.12345))
    # 最后一种格式化字符串的方法是使用以f开头的字符串，称之为f-string，它和普通字符串不同之处在于，字符串如果包含{xxx}，就会以对应的变量替换：
    r = 3
    PI = 3.1415926
    s = PI * r**2
    print(f'The Area of the circle with radius {r} is {s:.2f}')
    # Quiz: 小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
    this_year = 85
    last_year = 72
    increase = (this_year - last_year) / last_year *100
    print('小明的成绩提升了%.2f%%' % (increase))
    print()

    # Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素
    players = ['Tom', 'Taylor', 'Tao']
    print(players)
    # 用len()函数可以获得list元素的个数
    print(len(players))
    # 用索引来访问list中每一个位置的元素，记得索引是从0开始的, 记得最后一个元素的索引是len(list)-1 或 -1
    print(players[0], players[-1], players[-2])
    # list是一个可变的有序表，所以，可以往list中追加元素到末尾：
    players.append('wtj')
    print(players)
    # 也可以把元素插入到指定的位置，比如索引号为1的位置：
    players.insert(1,'wtl')
    print(players)
    # 要删除list末尾的元素，用pop()方法：
    players.pop()
    print(players)
    # 要删除指定位置的元素，用pop(i)方法，其中i是索引位置：
    players.pop(1)
    print(players)
    # 要把某个元素替换成别的元素，可以直接赋值给对应的索引位置：
    players[2] ='FT'
    print(players)
    # list里面的元素的数据类型也可以不同，比如：
    profiles = ['Tom', 180.25, 80.19, 'TOR', True]
    print(profiles)
    # list元素也可以是另一个list，比如：
    profiles_2 = ['Tom', [180.25, 80.19], 'TOR', True]
    print(len(profiles_2))
    # 如果一个list中一个元素也没有，就是一个空的list，它的长度为0：
    empty_list = []
    print(len(empty_list))
    print()

    # 另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改，比如同样是列出同学的名字：
    # 不可变的tuple有什么意义？因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。
    players_tp = ('Tom', 'Tao', 'Taylor')
    # 只有1个元素的tuple定义时必须加一个逗号,，来消除歧义
    tp = (1,)
    print(tp)
    # 最后来看一个“可变的”tuple：
    players_tp_2 = ('Tom', 'Tao', [170, 167])
    print(players_tp_2)
    players_tp_2[2][0] = 75
    players_tp_2[2][1] = 55
    print(players_tp_2)
    # 如果要定义一个空的tuple，可以写成()：
    tp = ()
    print(len(tp))
    print()

    # 条件判断
    height = 1.75
    weight = 80.5
    bmi = weight / (height**2)
    print("%.4f" % (bmi))
    if bmi < 18.5:
        print('too light')
    elif bmi < 25:
        print('normal')
    elif bmi < 28:
        print('too heavy')
    elif bmi < 32:
        print('obese')
    else:
        print('severely obese')
    print()

    # 循环
    # Python的循环有两种，一种是for...in循环，依次把list或tuple中的每个元素迭代出来，看例子：
    players = ['Tom', 'Tao', 'Taylor']
    for player in players:
        print(player)
    # 如果要计算1-100的整数之和，从1写到100有点困难，幸好Python提供一个range()函数，
    # 可以生成一个整数序列，再通过list()函数可以转换为list。比如range(5)生成的序列是从0开始小于5的整数：
    # range(start, stop, step)
    numbers = list(range(1,101))
    sum = 0
    for number in numbers:
        sum += number
    print(sum)
    # 第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环。比如我们要计算100以内所有奇数之和，可以用while循环实现：
    sum = 0
    n = 1
    while n < 100:
        sum += n
        n += 2
    print(sum)
    # Quiz: 请利用循环依次对list中的每个名字打印出Hello, xxx!：
    players = ['Tom', 'Tao', 'Taylor']
    for player in players:
        print('Hello, %s' % (player))
    print()

    # 使用dict和set
    # Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
    player_ages = {'Tom': 37, 'Tao': 35, 'Taylor': 1}
    print(player_ages['Tom'])
    # 把数据放入dict的方法，除了初始化时指定外，还可以通过key放入
    # 由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉
    player_ages['WTJ'] = 40
    player_ages['WTJ'] = 39
    print(player_ages['WTJ'])
    # 要避免key不存在的错误，有两种办法，一是通过in判断key是否存在：
    print('FT' in player_ages)
    print('Taylor' in player_ages)
    # 二是通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value：
    print(player_ages.get('FT'))
    print(player_ages.get('Taylor'))
    print(player_ages.get('FT', -1))
    # 要删除一个key，用pop(key)方法，对应的value也会从dict中删除：
    print(player_ages)
    player_ages.pop('WTJ')
    print(player_ages)
    # dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象
    # 这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）。
    # 要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key
    print()

    # set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
    # 要创建一个set，需要提供一个list作为输入集合
    test_set = set([1, 2, 3])
    print(test_set)
    # 重复元素在set中自动被过滤
    test_set = set([1,1,2,2,3,3,4])
    print(test_set)
    # 通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果
    test_set.add(5)
    print(test_set)
    # 通过remove(key)方法可以删除元素
    test_set.remove(5)
    print(test_set)
    # set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
    # 集合运算用 & | 不用 and or
    set_1 = set([1, 2, 3])
    set_2 = set([2, 3, 4])
    print(set_1 and set_2)
    print(set_1 or set_2)
    print(set_1 - set_2)
    # set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，所以，同样不可以放入可变对象，
    # 因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。

    # 再议不可变对象
    # 对于可变对象，比如list，对list进行操作，list内部的内容是会变化的，比如
    a = ['a', 'c', 'b']
    print(a)
    a.sort()
    print(a)
    # 而对于不可变对象，比如str，对str进行操作
    a = 'abc'
    print(a)
    print(a.replace('a', 'A'))
    print(a)
    print()

    # str 's replace method creates a new string, but not change the old str
    # 对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。相反，这些方法会创建新的对象并返回，
    # 这样，就保证了不可变对象本身永远是不可变的
    # REF: https://www.liaoxuefeng.com/wiki/1016959663602400/1017104324028448
    a = 'abc'
    b = a.replace('a', 'A')
    print('a = %s' % a)
    print('b = %s' % b)
    print()


