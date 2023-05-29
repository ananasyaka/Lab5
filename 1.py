from random import randint
a = [randint(-100, 100) for i in range(5)]
b = int(input ("Введите число "))
print (a)
print (b)
if b in a:
    print("Поздравляю, Вы угадали число!")
else:
    print("Нет такого числа!")