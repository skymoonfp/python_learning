#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     client.py
 IDE：    PyCharm
创建时间： 2019/5/30 16:29
@author： skymoon
"""

import pickle
import threading
import time

from client.plugins import plugin_api
from client.redis_helper import RedisHelper

host_ip = "192.168.1.135"


class MonitorClient(object):
    def __init__(self, server, port):
        self.server = server
        self.port = port
        self.configs = {}
        self.redis = RedisHelper()

    def format_msg(self, key, value):
        msg = {key: value}
        return pickle.dumps(msg)

    def get_configs(self):
        config = self.redis.get("HostConfig::%s" % host_ip)
        if config:
            self.configs = pickle.loads(config)
            return True

    def handle(self):
        if self.get_configs():
            print("----goint to monitor services----", self.configs)

            while True:
                for service_name, val in self.configs["services"].items():
                    # print(service_name, val)
                    interval, plugin_name, last_check = val
                    if time.time() - last_check >= interval:
                        # need to kick off the next run
                        t = threading.Thread(target=self.task, args=[service_name, plugin_name])
                        t.start()
                        self.configs["services"][service_name][2] = time.time()  # update last check time
                    else:
                        next_run_time = interval - (time.time() - last_check)
                        print("\033[22;34m%s\033[0m will be run in next \033[22;31m%f\033[0m seconds" % (
                            service_name, next_run_time))
                time.sleep(1)
        else:
            print("----could not found any configurations for this host----")

    def task(self, service_name, plugin_name):
        print("----going to run service:", service_name, plugin_name)
        func = getattr(plugin_api, plugin_name)
        result = func()
        # self.redis.publish(pickle.dumps(result))
        msg = self.format_msg("report_service_data",
                              {"ip": host_ip,
                               "service_name": service_name,
                               "data": result
                               })
        self.redis.publish(msg)

    def run(self):
        self.handle()


def main():
    cli = MonitorClient("YourMonitorServerIp", "port")
    cli.run()


if __name__ == "__main__":
    main()
