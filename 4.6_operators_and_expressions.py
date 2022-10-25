#average
from random import randint

num_1 = randint(0, 100)
num_2 = randint(0, 100)
num_3 = randint(0, 100)

print(f"3 случайных числа: {num_1, num_2, num_3}")
print(f"Среднее значение 3 случайных чисел = {int((num_1 + num_2 + num_3) / 3)}.")

#division
num_1 = randint(0, 100)
num_2 = randint(0, 100)

print(f"x = {num_1} и y = {num_2}")
print(f"{num_1 // num_2}, {num_1 % num_2}")

#float number
float_number = 10.156

print(f"x = {float_number}")
print(f"До двух знаков после запятой: {round(float_number, 2)}")
print(f"До целого: {round(float_number)}")
print('До 11 знаков: ''{:011}'.format(float_number))