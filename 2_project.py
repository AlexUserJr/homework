##Перевірка на просте число: Створіть функцію, яка приймає число як аргумент і повертає True, якщо число є простим, і False інакше.

num = int(input("Введіть число: "))

is_simple = True
if num >= 4:
    for i in range(2, num-1):
        if num%i == 0:
            is_simple = False
            break

if is_simple:
    print(is_simple)
else:
    print(is_simple)