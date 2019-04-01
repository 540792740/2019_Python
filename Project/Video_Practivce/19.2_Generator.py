a  = [x for x in range(5)]
print(a)

x  = (x for x in range(5))
print(x)
print(next(x))
# print(next(x))
print(next(x))
# generator, can be used in one time, cannot change
for x in (x):
    print(x)

# Fibonacci
# 1 1 2 3 5 7 12
def Fibonacci1(number):
    list = []
    list.append(1)
    count = 1
    list.append(1)
    count += 1
    while True:
        if list[count - 1] + list[count - 2] < number:
            list.append(list[count - 1] + list[count - 2])
            count += 1
        else:
            break

    return list
def Fobonacci2(times):
    count = 1
    a = 0
    b = 1
    while count < times:
        yield b #stop and dont excute
        a, b = b, a + b
        count += 1
        # print(b)
    return "done"
def generator1(time):
    n = 0
    while n < time:
        yield n*2
        n += 1
    return "done"

print(Fibonacci1(100))
g = Fobonacci2(10)
print(next(g))
# for x in g:
#     print(x)
print(g.send("k"))
print(g.send("123"))
g = generator1(10)
print(g.send(None))
# The very first number must be None
print(g.send("123"))
for x in g:
    print(x)