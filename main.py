"""Домашнее задание на темы Списки и Рекурсия."""


def passing_matrix(my_input: list, x: int, y: int, col: int, row: int) -> None:
    """Обход матрицы."""
    if x < 0 or x > row or y < 0 or y > col:
        print(f"Значения вне диапазона: x = {x}, y = {y}")
        # выходить ли из программы, если следующее действие вызовет исключение?

    if my_input[x][y] == 0:
        return None

    """Отмечаем ячейку как пройденную"""
    my_input[x][y] = 0

    """Сдвигаемся  вверх, вниз, вправо, влево для проверки кратера"""


    if x > 0:
        passing_matrix(my_input, x - 1, y, col, row)
    if x > row - 1:
        passing_matrix(my_input, x + 1, y, col, row)
    if y > 0:
        passing_matrix(my_input, x, y - 1, col, row)
    if y > col - 1:
        passing_matrix(my_input, x, y + 1, col, row)



def calculate(my_input: list) -> int:
    """Считаем количество кратеров."""
    count = 0
    """длина строки"""
    row = len(my_input)
    """длина столбца"""
    col = len(my_input[0])

    for i in range(row):
        for j in range(col):
            if my_input[i][j] == 1:
                passing_matrix(my_input, i, j, col, row)
                count += 1
    return count


def read_from_file(path_file: str) -> list:
    """Чтение из файла и преобразование данных в массив."""
    with open(path_file, 'r') as file:
        massiv = []
        for line in file:
            num = list(map(int, line.split()))  # как обрабатывать что не можем преобразовать?
            massiv.append(num)
        if len(massiv) == 0:
            print("Не удалось прочитать массив")
        return massiv


my_input = read_from_file('file.txt')
count_craters = calculate(my_input)
print(count_craters)
