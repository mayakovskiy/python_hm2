#задача 34
'''
def count_vowels(phrase):
    vowels = "АЕЁИОУЫЭЮЯаеёиоуыэюя"
    count = 0
    for char in phrase:
        if char in vowels:
            count += 1
    return count

def check_rhythm(pooh_poem):
    phrases = pooh_poem.split()  # Разбиваем стихотворение на фразы по пробелам
    rhythm = None
    
    for phrase in phrases:
        words = phrase.split("-")  # Разбиваем фразу на слова по дефисам
        vowel_counts = [count_vowels(word) for word in words]
        
        # Если все слова в фразе содержат одинаковое количество гласных,
        # то это соответствует ритму.
        if all(count == vowel_counts[0] for count in vowel_counts):
            if rhythm is None:
                rhythm = "Парам пам-пам"
        else:
            rhythm = "Пам парам"
            break  # Если хоть одна фраза не соответствует ритму, можно завершить проверку
    
    return rhythm


pooh_poem = input("Введите стихотворение Винни-Пуха: ")

result = check_rhythm(pooh_poem)
print(result)
'''

#задача 36
def print_operation_table(operation, num_rows=6, num_columns=6):
    for row in range(1, num_rows + 1):
        for col in range(1, num_columns + 1):
            result = operation(row, col)
            print(result, end=" ")
        print()  # Переход на новую строку после завершения текущей строки

# Пример использования с операцией умножения
print_operation_table(lambda x, y: x * y)
