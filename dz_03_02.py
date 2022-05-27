"""
Вычислить число pi c заданной точностью d
Пример: при d = 0.001,  c= 3.141.
"""
from math import pi

d = 0.001
tochnost = len(str(d).split('.')[1])
print(str(pi)[:tochnost + 2])
