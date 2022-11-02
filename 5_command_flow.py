#1.Fizz Buzz
input_number = int(input("Введите целое число: "))

if input_number % 3 == 0 and input_number % 5 == 0:
    print('Fizz Buzz')
elif input_number % 3 == 0:
    print('Fizz')
elif input_number % 5 == 0:
    print('Buzz')
else:
    print(str(input_number))

#2.Оценка числа
input_number = int(input("Введите число: "))

if input_number % 2 != 0:
    print('Плохо')
elif input_number >= 2 and input_number <= 5 and input_number % 2 == 0:
    print('Неплохо')
elif input_number >= 6 and input_number <= 20 and input_number % 2 == 0:
    print('Так себе')
elif input_number > 20 and input_number % 2 == 0:
    print('Отлично')

#3.Последовательность
from random import randint

N = randint(1, 10)
numbers = []
print(f"Число: N = {N}")

for num in range(1, N+1):
    numbers.append(num)
print(f'результат: {"".join(map(str, numbers))}')

#4.Секретное сообщение
text = str(input("Введите текст: "))
result = ""
for character in text:
    if character.isupper() == True:
        result += character
print(result)

#5.Три слова
some_string = str(input("Введите строку: "))
count = 0

for word in some_string.split(" "):
    if word.isalpha():
        count += 1
    else:
        count = 0
if count == 3:
    print(f"'{some_string}', результат: {True}")
else:
    print(f"'{some_string}', результат: {False}")

#6.Мир захватили левши
strings = ["left", "right", "left", "stop"]
union_string = ",".join(strings)
result_string = union_string.replace('right', 'left')

print(f"{strings}, результат: '{result_string}'")