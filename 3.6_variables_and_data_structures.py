#Welcome to Python
name = 'Vladimir'
surname = 'Ryabcev'

print(f"Hello {name} {surname}! You just delved into Python. Great start!")

#Python art
thickness = 5
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1) + c + (c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2) + (c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2) + (c*thickness).center(thickness*6))

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness) + c + (c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

#title
text = 'hello world'
result = text.title()

print(result)

#money format
amount = 100500.157
result = '{:,.2f}'.format(amount)

print(result)

#mat designer
height = 21
width = height * 3

for stick_count in range(1, height, 2):
    print(('.|.' * stick_count).center(width, '-'))

print('ДОБРО ПОЖАЛОВАТЬ'.center(width, '-'))

for stick_count in range(height-2, 0, -2):
    print(('.|.' * stick_count).center(width, '-'))