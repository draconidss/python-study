import unittest


class String(unittest.TestCase):

    def test_method(self):
        s = "hello World"
        print(s.title())
        print(s.upper())
        print(s.lower())
        print(s.rstrip())
        print(len(s))
        self.assertEqual(True, True)

    def test_format(self):
        s = "hello {name}"
        print(s.format(name="world")) # hello world

        place = """world"""
        print(f"hello {place}") # hello world

        foo = "bar"
        print(f"{foo=}") # foo='bar'，3.8 新特性
        self.assertEqual(True, True)

    def test_slice(self):
        s = "hello world"
        print(s[0:5]) # hello, 从0开始，到5结束，不包括5
        print(s[6:]) # world, 从6开始，到结尾
        print(s[:5]) # hello, 从0开始，到5结束，不包括5
        print(s[-5:]) # world, 从倒数第5个开始，到结尾
        print(s[:-5]) # hello, 从0开始，到倒数第5个结束，不包括倒数第5个
        print(s[::2]) # hlowrd, 从0开始，到结尾，每隔2个取一个
        print(s[::-2]) # drwlh, 从结尾开始，到0，每隔2个取一个
        print(s[-2::-2]) # lo le, 从倒数第2个开始，到0，每隔2个取一个
        # 自动处理越界索引
        print(s[0:100]) # hello world
        print(s[-100:100]) # hello world
        s1 = 'a'
        print("s1[0]:", s1[-1])
        self.assertEqual(True, True)
