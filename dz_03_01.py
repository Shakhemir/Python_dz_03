"Найти НОК двух чисел"

a = int(input("Число a = "))
b = int(input("Число b = "))


def NOD(a, b):
    result = 1
    for i in range(2, min(a, b) + 1):
        if a % i == b % i == 0:
            result = i
    return result


def NOK(a, b):
    return a * b // NOD(a, b)


print(f'НОК({a}, {b}) = {NOK(a, b)}')
