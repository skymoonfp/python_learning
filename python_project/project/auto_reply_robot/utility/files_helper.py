#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     files_helper.py
 IDE：    PyCharm
创建时间： 2019/5/25 11:54
@author： skymoon
"""


class FilesProcess(object):
    """Create, read, write, alter, delete files."""

    def __init__(self, file_name):
        """File_name."""
        self.file_name = file_name

    def create(self):
        """Create file."""
        try:
            with open(self.file_name, "rb") as file:
                print("该文件已经存在！")
                return file
        except FileNotFoundError:
            with open(self.file_name, "wb") as file:
                return file

    def write(self, data, mode):
        """Write file."""
        pass


class ReadWriteFileProcess(FilesProcess):
    """Use read-write mode process files."""

    def write(self, data, mode):
        """Write file."""
        try:
            with open(self.file_name, mode) as file:
                file.write(data)
        except FileNotFoundError:
            with open(self.file_name, "wb") as file:
                file.write(data)
        except EOFError:
            with open(self.file_name, "wb") as file:
                file.write(data)

    def writelines(self, data, mode):
        """Write file in lines."""
        try:
            with open(self.file_name, mode) as file:
                file.writelines(data)
        except FileNotFoundError:
            with open(self.file_name, "wb") as file:
                file.writelines(data)
        except EOFError:
            with open(self.file_name, "wb") as file:
                file.writelines(data)

    def read(self, mode, return_form="str"):
        """Read file."""
        try:
            with open(self.file_name, mode) as file:
                file.writelines(data)
        except FileNotFoundError:
            with open(self.file_name, "wb") as file:
                file.writelines(data)
        except EOFError:
            with open(self.file_name, "wb") as file:
                file.writelines(data)
