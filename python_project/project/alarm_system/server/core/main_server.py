#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     main_server.py
 IDE：    PyCharm
创建时间： 2019/5/30 下午7:42
@author： skymoon
"""

from server.core import serialize
from server.core.action_process import action_process
from server.core.redis_helper import RedisHelper


class MonitorServer(object):
    def __init__(self, ip, port):  # 第2步：运行构造函数
        self.ip = ip
        self.port = port
        self.hosts = serialize.all_hosts_configs()
        self.redis = RedisHelper()

    def handle(self):
        serialize.flush_all_hosts_configs_into_redis()  # 第5步：将客户端主机配置信息装入redis
        redis_sub = self.redis.subscribe()  # 第6步：打开收音机，开始订阅
        while True:
            msg = redis_sub.parse_response()  # 第7步：接收客户端主机发布（广播）的监控信息
            print("recv:", msg)
            action_process(self, msg)  # 第8步：处理客户端主机发布的监控信息
            print("----waiting for new message----")

            # received data
            # for host, val in self.hosts["hosts"].items():
            #     print(host, val)

    def run(self):
        print("----starting monitor server----")
        self.handle()  # 第4步：

    def process(self):
        pass


def main():
    s = MonitorServer("redis_ip", "port")  # 第1步：实例化
    s.run()  # 第3步：


if __name__ == "__main__":
    main()
