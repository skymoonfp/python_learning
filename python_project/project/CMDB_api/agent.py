#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     agent
 IDE：    PyCharm
创建时间： 2019/6/12 18:29
@author： skymoon
"""

import json
import time
import urllib
from http import client


class Program(object):
    def __init__(self):
        # self.hostname = os.environ["HOSTNAME"]
        self.server_info = {"11": "111", "22": "222"}

    def execute(self):
        # server_info = dict()
        # ram = MemoryPlugin.MemoryPlugin()
        # ram_dict = ram.execute()
        # disk = DiskPlugin.DiskPlugin()
        # disk_dict = disk.execute()
        # server_info = {
        #     "ram": ram_dict,
        #     "disk": disk_dict,
        # }

        RequestData = {"data": self.server_info}
        params = urllib.parse.urlencode(json.dumps(RequestData)).encode('utf-8')
        self.requesturl("127.0.0.1", "8001", "/receive_server_info/", params, 30)

    def requesturl(self, host, port, source, params, timeout):
        headers = {"Content-type": "application/json"}
        try:
            conn = client.HTTPConnection(host, port, timeout)
            conn.request("POST", source, params, headers)
            response = conn.getresponse()
            original = response.read()
            print(original)
        except Exception as e:
            raise e
        return original


if __name__ == "__main__":
    times = 0
    while True:
        objProgram = Program()
        objProgram.execute()
        times += 1
        time.sleep(30000)
