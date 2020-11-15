import unittest

''' 此部分可以不写，
因为已经设置当前 test 的working directory与开发的程序一致
'''
'''
import sys
sys.path.append('..')
print(sys.path)
'''

from my_dict import MyDict

class TestMyDict(unittest.TestCase):

    # 可以在单元测试中编写两个特殊的setUp()和tearDown()方法。这两个方法会分别在每调用一个测试方法的前后分别被执行
    # 设想你的测试需要启动一个数据库，这时，就可以在setUp()方法中连接数据库，在tearDown()方法中关闭数据库，
    # 这样，不必在每个测试方法中重复相同的代码
    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown...')

    def test_init(self):
        my_dict = MyDict(a = 1, b = 'test')
        self.assertEqual(my_dict.a, 1)
        self.assertEqual(my_dict.b, 'test')
        self.assertTrue(isinstance(my_dict, dict))

    def test_key(self):
        my_dict = MyDict()
        my_dict['key'] = 'value'
        self.assertEqual(my_dict.key, 'value')

    def test_attr(self):
        my_dict = MyDict()
        my_dict.key = 'value'
        self.assertTrue('key' in my_dict)
        self.assertEqual(my_dict['key'], 'value')

    def test_key_error(self):
        my_dict = MyDict()
        with self.assertRaises(KeyError):
            value = my_dict['empty']

    def test_attr_error(self):
        my_dict = MyDict()
        with self.assertRaises(AttributeError):
            value = my_dict.empty


if __name__ == '__main__':
    unittest.main()
