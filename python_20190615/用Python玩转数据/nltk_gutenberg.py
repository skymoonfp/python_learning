#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     nltk_gutenberg
 IDE：    PyCharm
创建时间： 2019/6/15 13:09
@author： skymoon
"""

from nltk.corpus import gutenberg

print(gutenberg.fileids())
texts = gutenberg.words('shakespeare-macbeth.txt')
print(texts)
