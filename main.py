# Блок импортируемых библиотек
import numpy as np
import pandas as pd

# Блок вводимых параметров
array_type = str(input('Введите тип антенной решётки (rectangular - прямоугольная, hexagonal - гексагональная): '))
num_x = int(input('Введите количество излучателей в строке: '))
num_y = int(input('Ваедите количество излучателей в столбце: '))
step_x = float(input('Введите шаг антенной решётки по горизонтали, см: ')) * 10
step_y = float(input('Введите шаг антенной решётки по вертикали, см: ')) * 10

# Создание пустых массивов для хранения координат по оси Х и Y излучателей
x_cords = np.array([[.0] * num_x] * num_y)
y_cords = np.array([[.0] * num_x] * num_y)

# Генерация координат излучателей по введённым параметрам с учётом выбора типа антенной решётки
match array_type:

    # Генерация координат излучателей для антенной решётки гексагонального типа
    case 'hexagonal':
        for i in range(num_y):
            for j in range(num_x):
                if i % 2 == 0:
                    x_cords[i][j] = j * step_x
                    y_cords[i][j] = i * step_y
                else:
                    x_cords[i][j] = j * step_x + step_x / 2
                    y_cords[i][j] = i * step_y

    # Генерация координат излучателей для антенной решётки прямоугольного типа
    case 'rectangular':
        for i in range(num_y):
            for j in range(num_x):
                x_cords[i][j] = j * step_x
                y_cords[i][j] = i * step_y

    # Вывод сообщения об ошибке в случае неверного выбора типа решётки
    case _:
        print('Введён неверный тип решётки')

# Слияние массивов координат X и Y в один массив, преобразование его в DataFrame и запись в .csv файл
xy_cords = np.stack((x_cords.flatten(), y_cords.flatten()), axis=-1)
header = ['X', 'Y']
index = [i for i in range(num_x * num_y)]
xy_df = pd.DataFrame(xy_cords, index, header)

name = 'antenna_array.csv'
xy_df.to_csv(name, index=False)
