from seleniumtest.classtest import ClassTest

'''
子类
'''


class ClassChild(ClassTest):
    def test_inherit(self):
        self.open_baidu()


test = ClassChild()
test.test_inherit()
