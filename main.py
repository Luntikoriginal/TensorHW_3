import math

x = 0
y = 0
print("Начальная позиция: ({}, {})".format(x, y))
while True:
    print("Введите 1, чтобы начать движение")
    check = input()
    if check == "1":
        moveX = int(input("Введите смещение относительно оси X: "))
        moveY = int(input("Введите смещение относительно оси Y: "))
        x += moveX
        y += moveY
        print("Мы перешли в точку: ({}, {})".format(x, y))
    else:
        break

print("\nКвадратное уравнение ax^2 + bx + c = 0")
a = int(input("Введите коэф a:"))
b = int(input("Введите коэф b:"))
c = int(input("Введите коэф c:"))
D = b**2 - 4 * a * c
if D < 0:
    sqd = complex(0, math.sqrt(-D))
    print((-b + sqd)/(2 * a))
    print((-b - sqd) / (2 * a))
elif D == 0:
    print(-b / (2 * a))
else:
    print((-b + math.sqrt(D)) / (2 * a))
    print((-b - math.sqrt(D)) / (2 * a))
