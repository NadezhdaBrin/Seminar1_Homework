# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

number_XY = int(input('Введите номер координатной  четверти от 1 до 4'))

if number_XY == 1:
    print('X > 0; Y > 0')
elif  number_XY == 2:
    print('X < 0; Y > 0')  
elif  number_XY == 3:
    print('X < 0; Y < 0') 
elif  number_XY == 4:
    print('X > 0; Y < 0') 
else:
    print('Не правильные координаты') 