"""
Определите функцию, которая удаляет весь текст, следующий за любым из переданных маркеров комментариев.
Любые пробелы в конце строки также должны быть удалены.
Пример:
Входные данные:
«apples, pears # and bananas
grapes
bananas !apples          »
Выходные данные:
«apples, pears
grapes
bananas»
Функция может вызываться вот так:
result = function("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
"""

def clean_text(txt, markers):
    txt_lst = txt.split('\n')
    for i in range(len(txt_lst)):
        txt_lst[i] = txt_lst[i].rstrip()
        for j in markers:
            if j in txt_lst[i]:
                txt_lst[i] = txt_lst[i].split(j)[0]
    return '\n'.join(txt_lst)

result = clean_text("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
print(result)