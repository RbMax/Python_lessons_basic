
# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()
print("Задача-1")
num=1
fruits = ["яблоко", "банан", "киви", "арбуз"]

for el in fruits:
    print('{}.{:>7}'.format(num,el))
    num+=1

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
print("Задача-2")
list1 = ['l', 'i', 's', 't', '1']
list2 = ['l', '1','s']

for el_in_list1 in list1:
    for el_in_list2 in list2:
        if el_in_list1==el_in_list2:
            list1.remove(el_in_list2)

print(list1)


# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

print('Задача-3:')
intNum =[4,5,6,7,8,9,10]

i = 0
for el in intNum:
     if intNum[i] % 2 == 0:
         intNum[i] = intNum[i]/4
     else:
        intNum[i] = intNum[i]*2
     i+=1

print(intNum)





