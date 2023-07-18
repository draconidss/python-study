import unittest


class String(unittest.TestCase):
    def test_operator(self):
        # 乘方运算用两个 **
        print(f"乘方运算：", 3 ** 2)  # 9
        # 除法运算总是得到浮点数
        print(f"除法运算总是得到浮点数：", 4 / 2)  # 2.0
        # 除法运算得到浮点数，但结果无法保证精确
        print(f"除法运算不精确：", 10 / 3)  # 3.3333333333333335
        # 浮点数运算结果无法保证精确
        print(f"浮点数运算结果无法保证精确：", 0.1 + 0.2, )  # 0.30000000000000004
        self.assertEqual(True, True)
