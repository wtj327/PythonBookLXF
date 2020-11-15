#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 面向对象高级编程
# https://www.liaoxuefeng.com/wiki/1016959663602400/1017501628721248

def test_code():
    print()
    print('leanr_oop_adv starts ...')
    print()
    # 正常情况下，当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性
    class Student():
        pass

    student_1 = Student()

    # bind an attribute
    student_1.name = 'Tom'
    print(student_1.name)

    # bind a method
    def set_age(self, age):
        self.age = age

    from types import MethodType
    student_1.set_age = MethodType(set_age, student_1)
    student_1.set_age(37)
    print(student_1.age)

    # 给一个实例绑定的方法，对另一个实例是不起作用
    # 为了给所有实例都绑定方法，可以给class绑定方法
    def set_score(self, score):
        self.score = score

    Student.set_score = set_score
    # Test newly bind method
    student_1.set_score(90)
    print(student_1.score)
    # 通常情况下，上面的set_score方法可以直接定义在class中，
    # 但动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现
    print()

    # Python内置的@property装饰器可以把一个方法变成属性
    class Student2(object):

        @property
        def score(self):
            return self._score

        @score.setter
        def score(self, value):
            if not isinstance(value, int):
                raise ValueError('score must be an integer')
            if value < 0 or value > 100:
                raise ValueError('score must be between 0 and 100')
            self._score = value

    student_2 = Student2()
    student_2.score = 60
    print(student_2.score)
    print()

    # Quiz: 请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution
    class Screen(object):

        def __init__(self, width=1000, height=500):
            self._width = width
            self._height = height

        @property
        def width(self):
            return self._width

        @width.setter
        def width(self, value):
            self._width = value

        @property
        def height(self):
            return self._height

        @height.setter
        def height(self, value):
            self._height = value

        @property
        def resolution(self):
            return self._width * self._height

    # 测试:
    s = Screen()
    print(s.width, s.height)
    s.width = 1024
    s.height = 768
    print('resolution =', s.resolution)
    if s.resolution == 786432:
        print('测试通过!')
    else:
        print('测试失败!')

    print()

    # multiple inheritance 多重继承
    # 通过多重继承，一个子类就可以同时获得多个父类的所有功能
    class Animal(object):
        def show_type(self):
            print('I am an animal.')

    class Mammal(Animal):
        def show_type(self):
            print('I am a mammal.')

    class Bird(Animal):
        def show_type(self):
            print('I am a bird.')

    class Runnable(object):
        def run(self):
            print('running...')

    class Flybale(object):
        def fly(self):
            print('flying...')

    # 多重继承
    class Dog(Mammal, Runnable):
        pass

    class Parrot(Bird, Flybale):
        pass

    dog_1 = Dog()
    dog_1.show_type()
    dog_1.run()
    print()

    # MixIn
    # 在设计类的继承关系时，通常，主线都是单一继承下来的，例如，Ostrich继承自Bird。
    # 但是，如果需要“混入”额外的功能，通过多重继承就可以实现，比如，让Ostrich除了继承自Bird外，
    # 再同时继承Runnable。这种设计通常称之为MixIn。
    # 为了更好地看出继承关系，我们把Runnable和Flyable改为RunnableMixIn和FlyableMixIn。
    # 类似的，你还可以定义出肉食动物CarnivorousMixIn和植食动物HerbivoresMixIn，让某个动物同时拥有好几个MixIn：
    # class Dog(Mammal, RunnableMixIn, CarnivorousMixIn)
    # 由于Python允许使用多重继承，因此，MixIn就是一种常见的设计。
    # 只允许单一继承的语言（如Java）不能使用MixIn的设计

    # 定制类
    # __slots__ 限制对象可以绑定的属性
    # __len__()方法是为了能让class作用于len()函数

    # __str__()方法是为了能让class打印出的东西好看
    class Person(object):
        def __init__(self, name):
            self.name = name
        def __str__(self):
            return 'Object of Person, name: %s' % self.name
        # 再定义一个__repr__()
        # __str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，
        # 也就是说，__repr__()是为调试服务的
        __repr__ = __str__

    person_1 = Person('Tom')
    print(person_1)
    print()

    # 当调用不存在的属性时，比如score，Python解释器会试图调用__getattr__(self, 'score')
    # 来尝试获得属性，这样，我们就有机会返回score的值
    # 本节介绍的是最常用的几个定制方法，还有很多可定制的方法，请参考Python的官方文档
    class Chain(object):
        def __init__(self, path=''):
            self._path = path
        def users(self, user):
            return Chain('/users/%s' % user)
        def __getattr__(self, item):
            return Chain('%s/%s' % (self._path, item))
        def __str__(self):
            return 'GET %s' % self._path
        __repr__ = __str__

    print(Chain().users('michael').repos.test)
    # 测试
    if str(Chain().users('michael').repos.test) == 'GET /users/michael/repos/test':
        print('测试通过')
    else:
        print('测试失败')
    print()

    # 使用枚举类 enum
    # 实例有限且固定，使用枚举类

    # 两种定义枚举类的方式：
    # 方式1：直接使用Enum列出多个枚举值来创建枚举类
    import enum
    # 定义 Season 枚举类
    Season = enum.Enum('Season', ('Spring', 'Summer', 'Fall', 'Winter'))
    # 定义枚举类之后，可以直接通过枚举值访问，这些枚举值都是该枚举类的成员，每个成员有 name 和 value 两个属性
    # 其中，name 属性为该枚举值的变量名，value 属性为序号（序号通常从1开始）
    print(Season.Spring)
    print(Season.Spring.name)
    print(Season.Spring.value)
    print()
    # 根据枚举的name访问枚举对象
    print(Season['Summer'])
    # 根据枚举的value访问枚举对象
    print(Season(3))
    print()
    # __members__ 属性返回字典，包含了该枚举类的所有枚举实例：'name': <枚举实例: value>
    print(Season.__members__)
    # 可以遍历 __members__，注：items()方法把字典中每对key和value组成一个元组，并把这些元组放在列表中返回
    for key, member in Season.__members__.items():
        print(key, '->', member, ',', member.value)
    print()

    # 方式2：通过继承Enum来派生枚举类，
    # 在这种方式下可以为枚举类定义新的方法
    class Direction(enum.Enum):
        # 为序列值指定value值，格式：name = value
        East = 'E'
        South = 'S'
        West = 'W'
        North = 'N'
        # 为这个枚举类定义一个新的方法
        def info(self):
            print('This is an Enum class representing Direction %s' % self.value)

    # 直接访问枚举对象
    print(Direction.East)
    print(Direction.South.name)
    print(Direction.West.value)
    print()
    # 通过name访问枚举对象
    print(Direction['East'])
    print(Direction['East'].name)
    print(Direction['East'].value)
    print()
    # 通过value访问枚举对象
    print(Direction('S'))
    print(Direction('S').name)
    print(Direction('S').value)
    print()
    # 遍历该枚举类的所有实例
    for name, member in Direction.__members__.items():
        print('name = %s, member =' % name, member, ', value = %s' % member.value)
    print()

    # 可以定义枚举类的构造器：
    class CanadaProvince(enum.Enum):

        # 使用构造函数生成的对象，等号后面是调用构造函数时传入的参数
        Ontario = 'Ontario', 'ON'
        Quebec = 'Quebec', 'QC'
        Nova_Scotia = 'Nova Scotia', 'NS'
        New_Brunswick = 'New Brunswick', 'NB'
        Manitoba = 'Manitoba', 'MB'
        British_Columbia = 'British Columbia', 'BC'
        Prince_Edward_Island = 'Prince Edward Island', 'PE'
        Saskatchewan = 'Saskatchewan', 'SK'
        Alberta = 'Alberta', 'AB'
        Newfoundland_and_Labrador = 'Newfoundland and Labrador', 'NL'
        Northwest_Territories = 'Northwest Territories', 'NT'
        Yukon = 'Yukon', 'YT'
        Nunavut = 'Nunavut', 'NU'

        # 自定义构造函数，传入两个参数以生成对象
        def __init__(self, full_name, abbreviation):
            self._full_name = full_name
            self._abbreviation = abbreviation

        @property
        def full_name(self):
            return self._full_name

        @property
        def abbreviation(self):
            return self._abbreviation

    # Test CanadaProvince
    print(CanadaProvince.British_Columbia)
    print(CanadaProvince.British_Columbia.name)
    print(CanadaProvince.British_Columbia.full_name)
    print(CanadaProvince.British_Columbia.value)
    print(CanadaProvince.British_Columbia.abbreviation)
    print()

    # enum Quiz
    # 把Student的gender属性改造为枚举类型，可以避免使用字符串：
    @enum.unique  # unique装饰器可以帮助我们检查保证没有重复值
    class Gender(enum.Enum):
        Male = 0
        Female = 1

    class Student(object):
        def __init__(self, name, gender):
            self.name = name
            self.gender = gender

    # Test quiz
    bart = Student('Bart', Gender.Male)
    if bart.gender == Gender.Male:
        print('测试通过!')
    else:
        print('测试失败!')
    print()

    # 使用元类 metaclass
    # 实例的类型是 类， 类的 类型 是 type
    # Python的class的定义是运行时动态创建的，而创建class的方法就是使用type()函数
    # 通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，
    # 仅仅是扫描一下class定义的语法，然后调用type()函数创建出class

    # 例子，使用type()函数创建class
    # 先定义几个函数用于测试类的方法
    def foo1(self, name = 'World'):
        print('Hello, %s.' % name)
    def foo2(self, sex = 'Male'):
        print('Sex = %s' % sex)
    # 使用type()函数创建class, 依次传入3个参数:
    # 1. class的名称；
    # 2. 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
    # 3. class的方法名称与函数绑定
    Hello = type('Hello', (object,), dict(name = foo1, sex = foo2))
    # 生成1个实例
    hello_1 = Hello()
    # 调用实例的方法
    hello_1.name()
    hello_1.sex()
    # 打印Hello类的类型
    print(type(Hello))
    # 打印hello_1实例的类型
    print(type(hello_1))
    print()

    # metaclass
    # 除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass
    # 当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例
    # 但是如果我们想创建出类呢？那就必须根据metaclass创建出类，所以：先定义metaclass，然后创建类
    # 连接起来就是：先定义metaclass，就可以创建类，最后创建实例

    # 例子：使用metaclass 给自定义的MyList类增加一个add方法
    # 首先定义一个metaclass
    class ListMetaclass(type):
        # cls代表被动态修改的类
        # name代表被动态修改的类的名字
        # bases代表被动态修改的类的所有父类
        # attrs代表被动态修改的类的所有属性、方法组成的字典
        def __new__(cls, name, bases, attrs):
            attrs['add'] = lambda self, value: self.append(value)
            return type.__new__(cls, name, bases, attrs)

    # 当我们传入关键字参数metaclass时，魔术就生效了，它
    # 指示Python解释器在创建MyList时，要通过ListMetaclass.__new__()来创建，
    # 在此，我们可以修改类的定义，比如，加上新的方法，然后，返回修改后的定义
    class MyList(list, metaclass=ListMetaclass):
        pass

    my_list = MyList()
    print(my_list)
    my_list.add(1)
    print(my_list)
    print()

    # TODO: 尝试编写一个ORM框架
    ''' test code
    my_dict = dict(name='Tom', sex='Male')
    print(my_dict)
    print(getattr(my_dict, 'name', None))
    '''

































