#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""

"""

import json

a = "123"
b = "ff"
c = '非'
d = a
with open("ceshi.json", "w") as f:
    json.dump(a + "\n", f)
    json.dump(b + "\n", f)

with open("ceshi.json", "r+") as f:
    print(json.load(f))
    print(json.load(f))
