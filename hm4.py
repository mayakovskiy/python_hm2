#задача 22
n = int(input("Введите количество элементов в первом наборе: "))
m = int(input("Введите количество элементов во втором наборе: "))

set1 = []
set2 = []

print("Введите элементы первого набора:")
for i in range(n):
    element = int(input())
    set1.append(element)

print("Введите элементы второго набора:")
for i in range(m):
    element = int(input())
    set2.append(element)

set1 = set(set1)
set2 = set(set2)

intersection = set1.intersection(set2)

print("Уникальные элементы, встречающиеся в обоих наборах:")
for element in intersection:
    print(element)

