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
from nltk.probability import *


class BookTexts(object):

    def __init__(self, book_file):
        self.book_file = book_file
        self.author = book_file.split(".")[0].split("-")[0]
        self.book_name = book_file.split(".")[0].split("-")[1]

    # 书籍内容（单词）
    @property
    def texts_words(self):
        texts_words = gutenberg.words(self.book_file)
        # print(texts_words)
        return texts_words

    # 总词数
    @property
    def total_words_count(self):
        total_words_count = len(self.texts_words)
        # print(total_words_count)
        return total_words_count

    # 不同词数
    @property
    def diff_words_count(self):
        diff_words_count = len(set(self.texts_words))
        # print(diff_words_count)
        return diff_words_count

    # 指定词出现次数
    def word_count(self, word):
        word_count = self.texts_words.count(word)
        # print(word_count)
        return word_count

    # 满足特定条件的词
    # 长度大于12的词
    def length_word(self, word_length):
        length_words = [w for w in set(self.texts_words) if len(w) > word_length]
        # print(length_words)
        return len(length_words), length_words

    # 以什么开头的词
    def word_begin(self, word_begin):
        words_begin = [w for w in set(self.texts_words) if w.startswith(word_begin)]
        return len(words_begin), words_begin

    # 以什么结尾的词
    def word_end(self, word_end):
        words_end = [w for w in set(self.texts_words) if w.endswith(word_end)]
        return len(words_end), words_end

    # 包含什么的词
    def word_contain(self, word_contain):
        words_contain = [w for w in set(self.texts_words) if w.count(word_contain)]
        return len(words_contain), words_contain

    # 统计词频数
    def frequency(self, display_count, flag=0):
        # 不区分大小写
        if not flag:
            fd = FreqDist([w.lower() for w in self.texts_words if w.isalpha()])
        # 区分大小写
        else:
            fd = FreqDist([w for w in self.texts_words if w.isalpha()])
        fd.tabulate(display_count)
        return fd.B(), fd.N()

    # 特定词出现的频率
    def frequency_word(self, word):
        return FreqDist([w for w in self.texts_words]).freq(word)

    # 输出函数
    def print_data(self, word, word_length, word_begin, word_contain):
        print("\033[1;35m" + "书名：" + self.book_name + "\033[0m")
        print("\033[1;33m" + "作者：" + self.author + "\033[0m")
        print("文本单词：", self.texts_words)
        print("文本总词数：", self.total_words_count)
        print("文本不同词数：", self.diff_words_count)
        print("文本包含\"" + word + "\"：%d 次" % self.word_count(word))
        print("文本中单词长度大于" + str(word_length) + "的词有%d个，分别是：\n%s" % (
        self.length_word(word_length)[0], self.length_word(word_length)[1]))
        print("文本中以" + word_begin + "开头的单词有%d个，分别是：\n%s" % (
        self.word_begin(word_begin)[0], self.word_begin(word_begin)[1]))
        print("文本中包含" + word_contain + "的单词有%d个，分别是：\n%s" % (
        self.word_contain(word_contain)[0], self.word_contain(word_contain)[1]))
        print("\n")


if __name__ == "__main__":
    # 书籍清单
    books_list = gutenberg.fileids()
    print(books_list)
    book_texts = BookTexts(books_list[0])
    book_texts.print_data("Emma", 15, "cont", "cont")
    a, b = book_texts.frequency(20)
    print(a)
    print(b)
    print(book_texts.frequency_word("the"))
