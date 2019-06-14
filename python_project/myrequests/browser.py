#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     browser.py
 IDE：    PyCharm
创建时间： 2019/5/31 10:36
@author： skymoon
"""

import requests


def browser(url, brs):
    try:
        r = requests.get(url, headers=brs)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text[1000:2000]
    except:
        print("爬取失败")


if __name__ == "__main__":
    brs = {"user-agent": "Mozilla/5.0"}
    url = "https://www.amazon.cn/gp/product/B07BQNMYSM/ref=s9_acsd_hps_bw_c_x_1_w?pf_rd_m=A1U5RCOVU0NYF2&pf_rd_s=merchandised-search-3&pf_rd_r=T2M6DM23G49VB8GG46G5&pf_rd_t=101&pf_rd_p=dcad7350-e0c9-482c-9117-05a4df6972b7&pf_rd_i=116099071"
    print(browser(url, brs))
