# -*- coding: utf-8 -*-

height = input('身高(米）：')
h = float(height)
weight = input('体重（千克）：')
w = float(weight)
bmi = w / (h ** 2)
if bmi < 18.5:
    print('BMI = %.1f,  低于18.5：过轻' % (bmi))
elif bmi <= 25:
    print('BMI = %.1f,  18.5-25:正常' % (bmi))
elif bmi <= 28:
    print('BMI = %.1f,  25-28:过重' % (bmi))
elif bmi <= 32:
    print('BMI = %.1f,  28-32:肥胖' % (bmi))
elif bmi > 32:
    print('BMI = %.1f,  高于32：严重肥胖' % (bmi))
print('\n')
input('Please press Enter to exit!')
