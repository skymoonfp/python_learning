# 打印出满足条件（n<1000且奇数）的交叉级数结果
L = [10, 100, 1000, 10000, 100000, 1000000, 1e7]
for l in L:
    sum, n, b, x = 0, 0, -1, 0
    while n < l:
        if n % 2 == 0:
            n += 1
            continue
        a = (n + 1) / 2 + 1
        y = pow(b, a)
        x = 1 / n
        sum = sum + x * y
        n += 1
    sum = sum * 4
    print(l, '    ', sum)
print('\n')
input('Please press Enter to exit!')
