#!/usr/bin/env python3
# -*- coding:utf-8 -*-


'''
#定义去首位空格函数：
def headTrim(s):
    if s[0] == ' ':                         #判断首位是否空格：Y则去首
        s = s[1:len(s)]
        headTrim(s)
    else:
        return s


#定义去尾位空格函数：
def tailTrim(s):
    if s[len(s)-1] == ' ':                        #判断尾位是否空格：Y则去尾
        s = s[0:(len(s)-2)]
        tailTrim(s)
    else:
        return s
'''


# 定义去首位空格函数：
def headTrim(s):
    i = 0
    n = len(s)
    while i < n and s[i] == ' ':
        i = i + 1
    s = s[i:n]
    return s


# 定义去末位空格函数：
def tailTrim(s):
    i = 0
    n = len(s)
    while i < n and s[n - 1 - i] == ' ':
        i = i + 1
    s = s[0:n - i]
    return s


# 定义去首尾空格函数：
def trim(s):
    s = headTrim(s)
    s = tailTrim(s)
    return s


def main():
    s0 = input('请输入字符串： ')
    s = trim(s0)
    print('处理前的字符串是：\"%s\"' % s0)
    print('处理后的字符串是：\"%s\"' % s)


main()

'''
# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
'''
