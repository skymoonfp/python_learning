sum, n, b, x = 0.000, 0, -1, 0.000  # 失败
while n < 10:
    if n % 2 == 0:
        n += 1
        continue
    a = (n + 1) / 2 + 1
    y = pow(b, a)
    x = 1 / n
    sum = sum + (1 / n) * y
    n = n + 1
print('%.3f' % sum)

sum, n, b, x = 0.000, 0, -1, 0.000  # 打印出满足条件（n<10且奇数）的n
while n < 10:
    if n % 2 == 0:
        n += 1
        continue
    print(n)
    n += 1

sum, n, b, x = 0.000, 0, -1, 0.000  # 打印出满足条件（n<10且奇数）的1/n
while n < 10:
    if n % 2 == 0:
        n += 1
        continue
    print(1 / n)
    n += 1

sum, n, b, x = 0.000, 0, -1, 0.000  # 打印出满足条件（n<10且奇数）的1/n及其求和
while n < 10:
    if n % 2 == 0:
        n += 1
        continue
    x = 1 / n
    print(x)
    sum = sum + x
    print(sum)
    n += 1

sum, n, b, x = 0.000, 0, -1, 0.000  # 打印出满足条件（n<10且奇数）的1/n及其求交叉级数
while n < 10:
    if n % 2 == 0:
        n += 1
        continue
    a = (n + 1) / 2 + 1
    y = pow(b, a)
    x = 1 / n
    print(x)
    sum = sum + x * y
    print(sum)
    n += 1

sum, n, b, x = 0.000, 0, -1, 0.000  # 打印出满足条件（n<10且奇数）的交叉级数结果
while n < 10:
    if n % 2 == 0:
        n += 1
        continue
    a = (n + 1) / 2 + 1
    y = pow(b, a)
    x = 1 / n
    sum = sum + x * y
    n += 1
print(sum)

sum, n, b, x = 0, 0, -1, 0  # 打印出满足条件（n<1000且奇数）的交叉级数结果
while n < 1000:
    if n % 2 == 0:
        n += 1
        continue
    a = (n + 1) / 2 + 1
    y = pow(b, a)
    x = 1 / n
    sum = sum + x * y
    n += 1
sum = sum * 4
print(sum)
print('\n')
input('Please press Enter to exit!')
