import math


def quadratic(a, b, c=0):
    if not isinstance(a, (int, float)):
        raise TypeError('bad operand type')
    if not isinstance(b, (int, float)):
        raise TypeError('bad operand type')
    if not isinstance(c, (int, float)):
        raise TypeError('bad operand type')
    if b ** 2 - 4 * a * c < 0:
        return None
    else:
        x = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        y = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        return x, y


a, b, c = map(float, input('请依次输入二次方程a*x**2+b*x+c=0的系数：').split())
print('该方程的两个根是：', quadratic(a, b, c))
print('\n')
input('Please press Enter to exit!')
