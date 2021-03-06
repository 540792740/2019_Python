'''
python中没有关键词private
变量名以 ‘__’开头， 两个下划线即为私有

私有变量只能在类里面修改，不能实例化之后再修改。
'''

class user:
    def __init__(self, pw):
        if len(pw) > 6:
            self.__password = pw
        else:
            print('lens of password is not longer then 6')
    def __str__(self):
        return 'password%s'%self.__password
    def get_password(self):
        return self.__password

    # 当删除时自动调用
    def __del__(self):
        print('delete')

u1 =  user('1234567')

# This line will wrong cuz __password is private.
# u1.__password = '123436677'

print(u1.get_password())
print(u1)
# 必须所有指针全部消失/
u2 = u1

del u1
print('u1 delete')
del u2
print('u2 delete')