i = 0
names = ['Michael', 'Bob', 'Tracy']
scores = [95, 75, 85]
x = input('input your name: ')
while i < len(names):
    if x is names[i]:
        break
    i = i + 1
if i < len(names):
    print(x, '的成绩: ', scores[i])
else:
    print(x, '的成绩未知！')
print('\n')
input('Please press Enter to exit!')
