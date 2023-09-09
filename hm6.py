#tusk30
'''
a1 = int(input("Введите первый элемент прогрессии (a1): "))
d = int(input("Введите разность прогрессии (d): "))
n = int(input("Введите количество элементов (n): "))

# Инициализация массива для хранения элементов прогрессии
progression = []

# Заполнение массива элементами арифметической прогрессии
for i in range(n):
    an = a1 + i * d
    progression.append(an)

# Вывод элементов прогрессии
print("Элементы арифметической прогрессии:")
for element in progression:
    print(element)
'''
#tusk32 
# Ввод минимума и максимума диапазона
min_value = float(input("Введите минимальное значение диапазона: "))
max_value = float(input("Введите максимальное значение диапазона: "))

# Ввод списка (массива) значений
values = list(map(float, input("Введите элементы списка через пробел: ").split()))

# Инициализация списка для хранения индексов элементов в заданном диапазоне
indices_in_range = []

# Поиск и добавление индексов элементов в заданном диапазоне
for i in range(len(values)):
    if min_value <= values[i] <= max_value:
        indices_in_range.append(i)

# Вывод индексов элементов в заданном диапазоне
print("Индексы элементов в заданном диапазоне:")
for index in indices_in_range:
    print(index)
