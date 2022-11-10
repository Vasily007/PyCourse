#Последний с четными
int_numbers = [0, 1, 2, 3, 4, 5]
sum = 0
for even_index in int_numbers:
    if int_numbers.index(even_index) % 2 == 0:
        sum += even_index
result = sum * int_numbers[-1]
print(sum)
print(result)

#Max-min
numbers = [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
if not numbers:
    result = 0
else:
    result = max(numbers) - min(numbers)
print(result)

#Умная сортировка
numbers = (-20, -5, 10, 15)
numbers = list(numbers)
max_number = max(abs(min(numbers)), abs(max(numbers)))
numbers.sort(key=lambda number: abs(number) * max_number - (number < 0))
numbers = tuple(numbers)
print(numbers)

#Медиана
list = [1, 2, 3, 4, 5]
sorted_list = sorted(list)
list_length = len(list)
index = (list_length - 1) // 2

if (list_length % 2):
    print(sorted_list[index])
else:
    print (sorted_list[index] + sorted_list[index + 1] / 2.0)