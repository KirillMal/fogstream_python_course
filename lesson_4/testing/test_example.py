# coding=utf-8

import unittest

import sys


class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # Проверим, что s.split не работает, если разделитель - не строка
        with self.assertRaises(TypeError):
            s.split(2)


# class MyTestCase(unittest.TestCase):
#     @unittest.skip("demonstrating skipping")
#     def test_nothing(self):
#         self.fail("shouldn't happen")
#
#     @unittest.skipIf(5 < 4,
#                      "not supported in this library version")
#     def test_format(self):
#         # Tests that work for only a certain version of the library.
#         pass
#
#     @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
#     def test_windows_support(self):
#         # windows specific testing code
#         pass

# class SimpleWidgetTestCase(unittest.TestCase):
#     def setUp(self):
#         self.widget = Widget('The widget')
#
#     def tearDown(self):
#         self.widget.dispose()


# class NumbersTest(unittest.TestCase):
#     def test_even(self):
#         """
#         Test that numbers between 0 and 5 are all even.
#         """
#         for i in range(0, 6):
#             with self.subTest(i=i):
#                 self.assertEqual(i % 2, 0)




if __name__ == '__main__':
    unittest.main()
