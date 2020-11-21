#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def test_code():

    print('learn_io_syn starts...')
    print()

    # open a file and read it into a str
    # using the "with" method
    with open('./user_files/user_info.txt', 'r') as f:
        str_ = f.read()
        print(str_)
    print('File reading complete...')
    print()

    # 调用readlines()一次读取所有内容并按行返回list
    # 如果是配置文件，调用readlines()最方便
    with open('./user_files/user_info.txt', 'r') as f:
        for line in f.readlines():
            print(line.strip())
    print()

    # write a txt file
    with open('./user_files/contact_info.txt', 'w') as f:
        f.write('Room No.: \n')
        f.write('Street No.: 101\n')
        f.write('Street Name: Centre Ave\n')
        f.write('City: Toronto\n')
        f.write('Province: ON\n')
        f.write('Postal Code: M2M 2L7\n')
    print()

    # Summary: 在Python中，文件读写是通过open()函数打开的文件对象完成的。使用with语句操作文件IO是个好习惯
    str_ = '中文'
    print(str_)
    # 略
    print()

    # 操作文件和目录
    import os
    print(os.name)
    print()

    # 查看当前目录的绝对路径:
    print(os.path.abspath('.'))
    # 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来
    # 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符
    new_dir = os.path.join(os.path.abspath('.'), 'new_dir')
    print(new_dir)
    # 然后创建一个目录:
    if not os.path.exists(new_dir):
        os.mkdir(new_dir)
    # 删掉一个目录:
    if os.path.exists(new_dir):
        os.rmdir(new_dir)
    # 同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，
    # 这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名
    current_path = os.path.abspath('.')
    print(current_path)
    current_path_1 = os.path.split(current_path)
    print(current_path_1)
    print(os.path.split(r'D:\DataWTJ\MyRepo\PythonBookLXF\readme.md'))
    print()

    # 创建，复制，重命名，删除文件

    # 创建
    if not os.path.exists('./test_file'):
        os.mkdir('./test_file')

    with open('./test_file/test_file.txt', 'w') as f:
        f.write('Test writing...')

    # 复制
    ori_file_path = './test_file/test_file.txt'
    import time
    new_file_name = 'test_file' + '_' + str(int(time.time())) + '.txt'
    print(new_file_name)
    dest_file_path = os.path.join('./test_file/', new_file_name)
    print(dest_file_path)
    import shutil
    shutil.copyfile(ori_file_path, dest_file_path)

    # 重命名
    new_file_name = 'test_file' + '_' + str(int(time.time())+1) + '.txt'
    dest_file_path = os.path.join('./test_file/', new_file_name)
    os.rename('./test_file/test_file.txt', dest_file_path)

    # 删除文件
    import glob
    print(glob.glob(r'./test_file/*.txt'))
    for file_ in glob.glob(r'./test_file/*.txt'):
        os.remove(file_)
    print()

    # 列出当前目录下所有.py文件
    print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])
    print()

    # 序列化 pickling
    # file.write 只能存储 字符串
    # 如果想save/load 任何数据结构，得用pickling和unpickling
    # 例如：存储字典到文件，再从文件读取该字典
    import pickle
    dict_ = dict(name = 'Tom', sex = 'Male', age = '37')
    # pickling
    with open('./test_file/test_pickling.txt', 'wb') as f:
        pickle.dump(dict_, f)
    # unpickling
    with open('./test_file/test_pickling.txt', 'rb') as f:
        dict_2 = pickle.load(f)
    print(dict_2)
    print()
    # Pickle的问题和所有其他编程语言特有的序列化问题一样，就是它只能用于Python，
    # 并且可能不同版本的Python彼此都不兼容，因此，只能用Pickle保存那些不重要的数据，不能成功地反序列化也没关系

    # JSON
    # 如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，比如XML，
    # 但更好的方法是序列化为JSON，因为JSON表示出来就是一个字符串，可以被所有语言读取，
    # 也可以方便地存储到磁盘或者通过网络传输。JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便。
    # 由于JSON标准规定JSON编码是UTF-8，所以我们总是能正确地在Python的str与JSON的字符串之间转换
    # JSON 类型 与 Python 类型的对应关系如下
    '''
        JSON            Python
        {}              dict
        []              list
        "string"        str
        1234.56         int / float
        true / False    True / False
        null            None
    '''
    # 例子：将一个dict数据结构存储到JSON文件，并从JSON文件读取该dict数据结构
    import json
    dict_ = dict(name = 'Tom', sex = 'Male', age = '37')
    dict_2 = dict(name = 'Taylor', sex = 'Female', age = '1')
    list_ = [dict_, dict_2]
    print(list_)
    # write to JSON
    with open('./test_file/test_json.txt', 'w') as f:
        json.dump(list_, f, indent=2)
    # read from JSON
    with open('./test_file/test_json.txt', 'r') as f:
        list_2 = json.load(f)
    print(list_2)
    for dict_ in list_2:
        print(dict_)
    print()

    # ensure_ascii参数对结果的影响
    obj = dict(name='小明', age=20)
    s = json.dumps(obj, ensure_ascii=True)
    print(s)
    s = json.dumps(obj, ensure_ascii=False)
    print(s)







