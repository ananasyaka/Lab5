from random import randint

a = [randint(0, 10) for i in range(10)]
print(a)
b = [x for x in a if a.count(x) > 1]
print(b)
