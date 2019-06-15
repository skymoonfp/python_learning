#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     pyqt
 IDE：    PyCharm
创建时间： 2019/6/16 0:47
@author： skymoon
"""

import sys

from PyQt5.QtWidgets import *


class TestWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        # self.windowTitleChanged("A Simple Example for PyQt.")
        self.outputArea = QTextBrowser(self)
        self.helloButton = QPushButton(self.Utf8("Click Me"), self)
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.outputArea)
        self.layout().addWidget(self.helloButton)
        self.helloButton.clicked.connect(self.sayHello)

    def sayHello(self):
        self.outputArea.append(self.trUtf8("Hello, World!"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    testWdiget = TestWidget()
    testWdiget.show()
    sys.exit(app.exec_())
