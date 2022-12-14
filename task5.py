# 5. Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
# in
# - 3
# - 6
# - 2
# - 1
# out
# 5.099
# ___________________________________________________________________________________________________
import math

X1 = int(input("Введите координату X для первой точки: "))
Y1 = int(input("Введите координату Y для первой точки: "))
X2 = int(input("Введите координату X для второй точки: "))
Y2 = int(input("Введите координату Y для второй точки: "))
XY = math.sqrt((X2 - X1) ** 2 + (Y2 - Y1) ** 2)
print("Расстояние между точками равно: ", round(XY, 3))
