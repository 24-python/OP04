# 2.	Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения
# (с помощью кортежа, после return перечислить все значения через запятую):
# периметр квадрата, площадь квадрата и диагональ квадрата


def square(x):
    p = x * 4
    s = x * x
    d = x * (2 ** (1/2))
    return p, s, d


x = int(input("enter X: "))

print(square(x))
