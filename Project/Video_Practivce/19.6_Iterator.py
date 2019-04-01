from collections import Iterable
'''
Author: Jiawei Wang
CWID: 10431455
E-mail: peterwangjiawei@gmail.com
'''
# IS the first paremeter can be iterable?
# Generator is iterable
# can be iterable, maybe not iterator
print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance((), Iterable))
print(isinstance((x for x in range(6)), Iterable))
print(isinstance(100, Iterable))