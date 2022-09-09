# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях.

# n = 5
# a = [i ** 2 for i in range(n)]

n = int(input("Введите N: "))

numbers = list(range(-n,n+1))

x = int(input('Введите позицию элемента #1: '))
y = int(input('Введите позицию элемента #2: '))

for i in range(len(numbers)):
    mult= numbers[x-1]*numbers[y-1]

print(numbers)
print(mult)