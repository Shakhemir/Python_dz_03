"""
Начиная в вершине треугольника (см. пример ниже) и перемещаясь вниз на смежные числа,
максимальная сумма до основания составляет 23.
3
7 4
2 4 6
8 5 9 3
То есть, 3 + 7 + 4 + 9 = 23.
Найдите максимальную сумму пути от вершины до основания следующего треугольника:
...
"""

data_file = "triangle.txt"
# цвета для выделения максимального пути в пирамиде
accent_color = '\033[1;33m'
def_color = '\033[0m'


def ShowTriangle(tri, accent=None):
    """
    Функция для вывода пирамиды в консоли с возможностью выделения цветом
    :param tri: матрица с пирамидой
    :param accent: путь максимальной суммы в виде бинарного кода для выделения его цветом, например "01110101011"
                   если он пустой, то просто выводится пирамида без выделения цветом
    """

    space = len(tri) * (len(tri[0][0]) + 1)
    if accent is None:
        for line in tri:
            print(' '.join(line).center(space))
    else:
        pos = 0
        for i in range(len(accent)):
            pos += int(accent[i])
            line = ' '.join(tri[i]).split()
            line[pos] = accent_color + line[pos] + def_color
            print(' '.join(line).center(space + 9))

# считываем данные цифры из файла и заносим их в двумерный массив
with open(data_file, 'r') as file:
    data = file.read().strip()
tri_list = []
for line in data.split('\n'):
    tri_list.append(line.split())


def Max_tri_way(tri):
    """
    Функция для рассчета пути с максимальной суммой
    :param tri: двумерный массив с нашей пирамидой
    :return: возвращает значение максимальной суммы и бинарный код пути для вывода на экран с цветом
    """
    def summ_bin_way(bin_way):
        # тут производятся расчеты суммы по пути бинарного параметра bin_way
        pos = 0
        summ = 0
        for i in range(len(bin_way)):
            pos += int(bin_way[i])
            summ += int(tri[i][pos])
        return summ

    size = len(tri)
    max_combination = 2 ** (size - 1)  # узнаем максимальное количество возможных комбинаций
    max_summ = 0
    for i in range(max_combination):
        bin_way = bin(i)[2:].rjust(15, '0')  # переводим в бинарный код очередную комбинацию
        summ = summ_bin_way(bin_way)  # функция возвращает нужную сумму
        if summ > max_summ:
            max_summ = summ
            max_bin_way = bin_way
    return max_summ, max_bin_way

max_summ, bin_way = Max_tri_way(tri_list)  # производим все нужные рассчеты тут
ShowTriangle(tri_list, bin_way)  # вывод на экран
print(f'Максимальная сумма = {max_summ}')