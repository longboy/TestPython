from seleniumtest.classtest import ClassTest


class ClassChild(ClassTest):
    def test_inherit(self):
        self.open_baidu()


test = ClassChild()
test.test_inherit()
