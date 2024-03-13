##Розрахунок середнього значення: Напишіть функцію, щоб обчислити середнє значення списку чисел.

def average(num):
    if not num:
        return "it's not numbers"
    return sum(num) / len(num)

num = [1, 2, 3, 4, 5]
midle = average(num)

print(f"Середнє значення списку {num}: {midle}")