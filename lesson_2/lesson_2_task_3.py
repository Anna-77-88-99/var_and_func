import math

def square(side):
    rounded_side = math.ceil(side) if not isinstance(side, int) else side

    area = rounded_side ** 2
    return area

side = float(input("Введите длину стороны квадрата: "))
result = square(side)
print(f"Площадь квадрата с длиной {math.ceil(side)} равна {result}")