class Test(object):
    def __init__(self):
        self.__num = 100

    def getNum(self):
        return self.__num

    def setNum(self, num):
        if num < 100:
            self.__num = num
    num = property(getNum,setNum)
t = Test()
t.num = 20
print(t.num)

class Test(object):
    def __init__(self):
        self.__num = 100

    @property
    def num(self):
        return self.__num
    @num.setter
    def num(self, num):
        if num < 100:
            self.__num = num
t = Test()
t.num = 20
print(t.num)