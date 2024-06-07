import math

def square(side):
    if not isinstance(side, int):
        side = math.ceil(side)

    area = side * side
    return area

side = float(input("Введите длину стороны квадрата: "))
result = square(side)
print(f"Площадь квадрата с длиной {side} равна {result}")