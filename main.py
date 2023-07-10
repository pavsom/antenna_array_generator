# Блок импортируемых библиотек
import numpy as np

# Блок вводимых параметров
type = str(input('Введите тип антенной решётки (rectangular - прямоугольная, hexagonal - гексагональная): '))
num_x = int(input('Введите количество излучателей в строке: '))
num_y = int(input('Ваедите количество излучателей в столбце: '))
step_x = float(input('Введите шаг антенной решётки по горизонтали, см: '))
step_y = float(input('Введите шаг антенной решётки по вертикали, см: '))

x_coords = np.array([[.0] * num_x] * num_y)
y_coords = np.array([[.0] * num_x] * num_y)

match type:

    case 'hexagonal':
        for i in range(num_y):
            for j in range(num_x):
                if i % 2 == 0:
                    x_coords[i, j] = j * step_x
                    y_coords[i, j] = i * step_y
                else:
                    x_coords[i, j] = j * step_x + step_x / 2
                    y_coords[i, j] = i * step_y + step_y / 2

    case 'rectangular':
        for i in range(num_y):
            for j in range(num_x):
                x_coords[i, j] = j * step_x
                y_coords[i, j] = i * step_y

    case _:
        print('Введён неверный тип решётки')

print('hah')