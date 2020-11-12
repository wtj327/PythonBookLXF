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

    # 获取对象信息：当我们拿到一个对象的引用时，如何知道这个对象是什么类型、有哪些方法
    # Use type() to ge the type of object
    print(type(123))
    print(type('123'))
    print(type(None))
    print(type(abs))
    print(type('1234') == str)
    # Check if an object is a function
    import types
    def foo1():
        pass
    print(type(foo1) == types.FunctionType)
    print(type(abs) == types.BuiltinFunctionType)
    print(type(lambda x: x**2) == types.LambdaType)
    print(type(x**2 for x in range(1, 10, 1)))
    print(type(x ** 2 for x in range(1, 10, 1)) == types.GeneratorType)
    print()
    # 对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数
    # object -> Animal -> Dog -> Husky
    animal1 = Animal()
    dog1 = Dog()
    class Husky(Dog):
        def run(self):
            print('Husky is running')
    husky1 = Husky()
    print(isinstance(husky1, Husky))
    print(isinstance(husky1, Dog))
    print(isinstance(husky1, Animal))
    print(isinstance(husky1, object))
    print()
    # 能用type()判断的基本类型也可以用isinstance()判断
    print(isinstance('123', str))
    # 并且还可以判断一个变量是否是某些类型中的一种
    print(isinstance('123', (list, tuple, str)))
    print()

    # 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法
    print(dir('abc'))
    # 类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。
    # 在Python中，如果你调用len()函数试图获取一个对象的长度，
    # 实际上，在len()函数内部，它自动去调用该对象的__len__()方法，所以，下面的代码是等价的
    print(len('abc'))
    print('abc'.__len__())
    print()
    # 我们自己写的类，如果也想用len(myObj)的话，就自己写一个__len__()方法
    class GoldenRetriever(Dog):
        def __len__(self):
            return 100
    golden_retriever_1 = GoldenRetriever()
    print(len(golden_retriever_1))
    print()
    # 仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态
    class MyObj(object):
        def __init__(self):
            self.x = 9
        def power(self):
            return self.x ** 2

    my_obj_1 = MyObj()
    print(my_obj_1.x)
    # Check if the object has the designated attribute
    print(hasattr(my_obj_1, 'x'))
    print()

    # Set a new attribute to the object
    setattr(my_obj_1, 'y', 19)
    print(hasattr(my_obj_1, 'y'))
    print(my_obj_1.y)
    print()

    # Get the designated attribute of an object
    print(my_obj_1.y)
    print(getattr(my_obj_1, 'y'))
    print()

    # 如果试图获取不存在的属性，会抛出AttributeError的错误
    # 可以传入一个default参数，如果属性不存在，就返回默认值
    print(getattr(my_obj_1, 'z', 'DNE'))
    print()
    # 也可以获得对象的方法
    print(hasattr(my_obj_1, 'power'))
    print(getattr(my_obj_1, 'power'))
    foo = getattr(my_obj_1, 'power')
    # Call foo() is equivalent to call my_obj_1.power()
    print(foo())
    print()

    # 实例属性和类属性
    # 由于Python是动态语言，根据类创建的实例可以任意绑定属性。
    # 给实例绑定属性的方法是通过实例变量，或者通过self变量
    class Student(object):
        def __init__(self, name):
            self.name = name
    student_1 = Student('Tom')
    student_1.score = 90
    print(student_1.name)
    print(student_1.score)
    print()

    # 但是，如果Student类本身需要绑定一个属性呢？可以直接在class中定义属性，这种属性是类属性，归Student类所有
    class StudentB(object):
        name = 'Student'
    # 当我们定义了一个类属性后，这个属性虽然归类所有，但类的所有实例都可以访问到
    student_2 = StudentB()
    print(student_2.name)  # 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
    print(StudentB.name)  # 打印类的name属性
    student_2.name = 'Tao Feng'  # 给实例绑定name属性
    print(student_2.name)  # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
    print(StudentB.name)  # 但是类属性并未消失，用Student.name仍然可以访问
    del student_2.name  # 删除实例的name属性
    print(student_2.name) # 再次调用student_2.name，由于实例的name属性没有找到，类的name属性就显示出来了
    # 从上面的例子可以看出，在编写程序的时候，千万不要对实例属性和类属性使用相同的名字，
    # 因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性
    print()

    # Quiz: 为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加
    class Student(object):
        count = 0
        def __init__(self, name):
            self.name = name
            Student.count += 1
    # 测试:
    if Student.count != 0:
        print('测试失败!')
    else:
        bart = Student('Bart')
        if Student.count != 1:
            print('测试失败!')
        else:
            lisa = Student('Bart')
            if Student.count != 2:
                print('测试失败!')
            else:
                print('Students:', Student.count)
                print('测试通过!')


















