#задача 22
"""
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

"""

#задача 24
N = int(input("Введите количество кустов: "))
berries = []

print("Введите количество ягод на каждом кусте:")
for i in range(N):
    berry_count = int(input())
    berries.append(berry_count)


collected_berries = []
for i in range(N):
    collected = berries[i] + berries[(i + 1) % N] + berries[(i + 2) % N]
    collected_berries.append(collected)


max_collected = max(collected_berries)
max_position = collected_berries.index(max_collected) + 1 
print("Максимальное количество собранных ягод:", max_collected)
print("Позиция (номер куста), перед которой собрано максимальное количество ягод:", max_position)