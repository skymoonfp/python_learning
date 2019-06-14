#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     linux.py
 IDE：    PyCharm
创建时间： 2019/5/29 18:31
@author： skymoon
"""

from server.config.services import generic
from server.config.services.data_process import avg, hit


class Cpu(generic.BaseService):
    def __init__(self):
        super(Cpu, self).__init__()
        self.name = "linux_cpu"
        self.interval = 30
        self.plugin_name = "get_cpu_status"
        self.triggers = {
            "idle": {"func": avg,
                     "minutes": 15,
                     "operator": "lt",
                     "warning": 20,
                     "critical": 5,
                     "data_type": "percentage"
                     },
            "iowait": {"func": hit,
                       "minutes": 10,
                       "operator": "gt",
                       "threshold": 3,
                       "warning": 50,
                       "critical": 80,
                       "data_type": "int"
                       }
        }


class Memory(generic.BaseService):
    def __init__(self):
        super(Memory, self).__init__()
        self.name = "linux_memory"
        self.interval = 30
        self.plugin_name = "get_memory_info"
        self.triggers = {
            "usage": {"func": avg,
                      "minutes": 15,
                      "operator": "gt",
                      "warning": 80,
                      "critical": 90,
                      "data_type": "percentage"
                      }
        }


if __name__ == "__main__":
    pass
