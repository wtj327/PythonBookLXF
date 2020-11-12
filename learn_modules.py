#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Modules

def test_code():

    print('Start of learning modules')
    print()
    # 在Python中，一个.py文件就称之为一个模块（Module）
    # 请注意，每一个包目录下面都会有一个__init__.py的文件，这个文件是必须存在的，
    # 否则，Python就把这个目录当成普通目录，而不是一个包。__init__.py可以是空文件，
    # 也可以有Python代码，因为__init__.py本身就是一个模块，而它的模块名就是mycompany

    # test the use of sys module
    import sys
    args = sys.argv  # sys模块有一个argv变量，用list存储了命令行的所有参数。argv至少有一个元素，因为第一个参数永远是该.py文件的名称
    print(args)
    print('End of learning modules')
    print()
































