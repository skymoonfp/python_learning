#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 定义乘积函数
def product(*numbers):
    s = 1
    for n in numbers:
        s = s * n
    return s


# 测试
print('product(5)=', product(5))
print('product(5,6)=', product(5, 6))
print('product(5,6,7)=', product(5, 6, 7))
print('product(5,6,7,9)=', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败！')
elif product(5, 6) != 30:
    print('测试失败！')
elif product(5, 6, 7) != 210:
    print('测试失败！')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败！')
else:
    try:
        product()
        print('测试成功！')
    except TypeError:
        print('测试成功！')


# 定义输出格式函数
def print_input(*numbers):
    if len(numbers) == 1:
        print('product(%s)=%s' % (numbers[0], product(*numbers)))
    else:
        # print('product%s=%f' %(''.join(repr(numbers)),product(*numbers)))
        print('product%s=%s' % (numbers, product(*numbers)))


# 输入数据
numbs = map(float, input('Enter numbers：').split())
print_input(*numbs)

print('\n')
input('Please press Enter to exit!')
