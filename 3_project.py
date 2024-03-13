##Підрахунок кількості голосних букв у рядку: Напишіть функцію, яка приймає рядок як аргумент і повертає кількість голосних букв у цьому рядку.

def count_(string):
  v = "aeiouAEIOU"
  count = 0
  for char in string:
    if char in v:
      count += 1
  return count
