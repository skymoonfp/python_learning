#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     ip.py
 IDE：    PyCharm
创建时间： 2019/5/31 12:06
@author： skymoon
"""

import requests


# def ip_check(url, ip):
#
#     ip = {"ip": ip}
#
#     try:
#         r = requests.get(url, params=ip)
#         r.raise_for_status()
#         return r.text
#     except Exception as e:
#         print(e)
#         print("爬取失败")
#
#
# if __name__ == "__main__":
#     url = "http://www.ip138.com/ips138.asp"
#     ip = "192.12.13.111"
#     print(ip_check(url, ip))


# def ip_check(url, ip):
#
#     try:
#         r = requests.get(url + ip)
#         r.raise_for_status()
#         return r.text
#     except Exception as e:
#         print("\033[35m")
#         print(e)
#         print("\033[0m")
#         print("爬取失败")
#
#
# if __name__ == "__main__":
#     url = "http://www.ip138.com/ips138.asp?ip="
#     ip = "192.12.13.111"
#     print(ip_check(url, ip))


def ip_check(url, ip):

    try:
        r = requests.get(url + ip)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except Exception as e:
        print("\033[35m")
        print(e)
        print("\033[0m")
        print("爬取失败")


if __name__ == "__main__":
    url = "http://www.ip138.com/ips1388.asp?ip="
    ip = "192.12.13.111"
    print(ip_check(url, ip))
