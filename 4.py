import random
a = ["Пугачев","Иванова","Кулебякина","Андреева","Щербаков","Иванов","Голубцова","Евсеев","Золина","Рыжиков"]
b = ["Никитина","Вяткин","Рябов","Кузнецова","Денисов","Саватеева","Калинин","Васнецова","Золотухин","Евтушенко"]
print (a)
print (b)
random.shuffle(a)
random.shuffle(b)
komanda = (tuple(sorted(a[:5]+b[:5])))
print(komanda)
print ("Длина =",len(komanda))
n=0
for x in komanda:
 if x == 'Иванов':
  n=n+1
if n>0:
 print ("Иванов входит в команду, фамилия встречается",n,"раз")
else:
 print ("Иванов не входит в команду")
