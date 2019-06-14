#!/usr/bin/env python3
# coding=utf-8


file1 = open('E:\DataAnalysis\Python_code\TeleAddressBook.txt', 'rb')
file2 = open('E:\DataAnalysis\Python_code\EmailAddressBook.txt', 'rb')

file1.readline()  # 跳过第一行
file2.readline()
lines1 = file1.readlines()
lines2 = file2.readlines()

list1_name = []
list1_tele = []
list2_name = []
list2_email = []
lines = []

for line in lines1:  # 获得第一个文本中的姓名和电话信息
    elements = line.split()
    list1_name.append(str(elements[0].decode('gbk')))
    list1_tele.append(str(elements[1].decode('gbk')))

for line in lines2:  # 获得第二个文本中的姓名和邮件信息
    elements = line.split()
    list2_name.append(str(elements[0].decode('gbk')))
    list2_email.append(str(elements[1].decode('gbk')))

# 按索引方式遍历姓名列表1
for i in range(len(list1_name)):
    s = ''
    if list1_name[i] in list2_name:
        j = list2_name.index(list1_name[i])  # 找到姓名列表1中姓名对应列表2中姓名在列表2中的索引号
        s = '\t'.join([list1_name[i], list1_tele[i], list2_email[j]])
        s += '\n'
    else:
        s = '\t'.join([list1_name[i], list1_tele[i], str('   -----   ')])
        s += '\n'
    lines.append(s)

# 处理姓名列表2中剩余的姓名
for i in range(len(list2_name)):
    s = ''
    if list2_name[i] not in list1_name:
        s = '\t'.join([list2_name[i], str('   -----   '), list2_email[i]])
        s += '\n'
    lines.append(s)

file3 = open('AddressBook.txt', 'w')
file3.writelines(lines)

file1.close()
file2.close()
file3.close()

print("The addressBook are merged!")
