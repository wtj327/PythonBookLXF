#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Modules

def test_code():
    # 在Python中，所有数据类型都可以视为对象，当然也可以自定义对象。自定义的对象数据类型就是面向对象中的类（Class）的概念
    print('Start of learning oop basics')
    print()

    # Test class
    class Student0(object):

        def __init__(self, name, score):
            self.name = name
            self.score = score

        def print_score(self):
            print('%s: %.2f' % (self.name, self.score))

    # create instances
    tianjiao = Student0('Tianjiao Wang', 89)
    tao = Student0('Tao Feng', 95)
    tianjiao.print_score()
    tao.print_score()
    print()

    # 访问限制
    # 在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
    class Student2(object):

        def __init__(self, name, score):
            self.__name = name
            self.__score = score

        def print_score(self):
            print('%s: %.1f' % (self.__name, self.__score))

    tianjiao2 = Student2('Tianjiao Wang', 89)
    tao2 = Student2('Tao Feng', 95)
    tianjiao2.print_score()
    tao2.print_score()
    print()
    # print(tianjiao2.__name) does not work
    # to access private attributes, we need to add the corresponding methods

    class Student3(object):

        def __init__(self, name, score):
            self.__name = name
            self.__score = score

        def print_score(self):
            print('%s: %.1f' % (self.__name, self.__score))

        def get_name(self):
            return self.__name

        def get_score(self):
            return self.__score

        def set_name(self, name):
            self.__name = str(name)

        def set_score(self, score):
            self.__score = score

    tianjiao3 = Student3('Tianjiao Wang', 89)
    tao3 = Student3('Tao Feng', 95)
    tianjiao3.print_score()
    tao3.print_score()
    print(tianjiao3.get_name())
    tianjiao3.set_name('Tom Wang')
    print(tianjiao3.get_name())
    print()

    # 需要注意的是，在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，
    # 特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名
    # 有些时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，
    # 但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”

    # Quiz
    class Student(object):
        def __init__(self, name, gender):
            self.name = name
            self.__gender = gender

        def get_gender(self):
            return self.__gender

        def set_gender(self, gender):
            self.__gender = gender

    # 测试:
    bart = Student('Bart', 'male')
    if bart.get_gender() != 'male':
        print('测试失败!')
    else:
        bart.set_gender('female')
        if bart.get_gender() != 'female':
            print('测试失败!')
        else:
            print('测试成功!')
    print()

    # 继承和多态
    # 当子类和父类都存在相同的run()方法时，我们说，子类的run()
    # 覆盖了父类的run()，在代码运行的时候，总是会调用子类的run()。这样，我们就获得了继承的另一个好处：多态
    class Animal(object):

        def run(self):
            print('Animal is running')

    class Cat(Animal):

        pass

    class Dog(Animal):

        def run(self):
            print('Dog is running')

    cat1 = Cat()
    dog1 = Dog()
    cat1.run()
    dog1.run()
    print()
    # 判断一个变量是否是某个类型可以用isinstance()判断
    print(isinstance(cat1, Cat))
    print(isinstance(dog1, Dog))
    print(isinstance(dog1, Animal))
    print(isinstance(dog1, object))
    print()
    # 展示多态的威力
    # define a new function
    def run_twice(animal):
        animal.run()
        animal.run()
    # Call the above function
    run_twice(Animal())
    run_twice(Dog())
    # define a new class
    class Duck(Animal):
        def run(self):
            print('Duck is running')
    run_twice(Duck())
    print()
    # 对于Python这样的动态语言来说，不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了
    class Timer(object):
        def run(self):
            print('Start...')
    run_twice(Timer())
    print()
    # Summary
    # 继承可以把父类的所有功能都直接拿过来，这样就不必重零做起，子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写。
    # 动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的。

















