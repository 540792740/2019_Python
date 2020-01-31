from collections import Iterator
# 1.
g = (x for x in range(5, 10))
print(next(g))
print(next(g))
# 2.
def fibonacci(times):
    n = 0
    a, b = 0, 1
    while n < times:
        yield b
        a, b = b, a + b
        n += 1
    return 'done'
g = fibonacci(5)
print('fibonacci', next(g))

# 3. Iterator
'''
    Iterable: list, tuple, dict, set, str
        yield(generator) can be iterator
'''
print(isinstance(100, Iterator))

# 4. Decorator:
'''
1. Don't change past code. just try to add more code on it.
        make function completely
'''
print('Decorator---------------------------------')
# 通用装饰器
def func1(func2):
    def wrapped():
        print('wrapped in function1')
        return func2()
    return wrapped
@func1
def test1():
    return 'Test1'
print(test1())