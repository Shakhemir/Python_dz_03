"Составить список простых множителей натурального числа N"

prime_list = [2]


# Эта функция составляет список из N простых чисел, для последущих операций
def fill_prime_list(to_number):
    to_number = int(to_number)
    for i in range(3, to_number + 1):
        if i > 10 and i % 10 == 5:
            continue
        for j in prime_list:
            if j * j - 1 > i:
                prime_list.append(i)
                break
            if i % j == 0:
                break
        else:
            prime_list.append(i)


N = int(input("N = "))
fill_prime_list(N)  # заполняем список простых чисел
mnojiteli = []  # тут будут множители
mnojiteli_str = ''  # множители для удобства вывода в текстовом виде
chastnoe = N
while chastnoe not in prime_list:
    for i in prime_list:
        if chastnoe % i == 0:
            mnojiteli.append(i)
            mnojiteli_str += f'{i} * '
            chastnoe //= i
            break
mnojiteli.append(chastnoe)
mnojiteli_str += str(chastnoe)
print(mnojiteli)
print(f'{N} = {mnojiteli_str}')
