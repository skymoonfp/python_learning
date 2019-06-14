#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     serialize.py
 IDE：    PyCharm
创建时间： 2019/5/30 10:19
@author： skymoon
"""

import pickle
# import global_settings
import time

from server.config import hosts
from server.core.redis_helper import RedisHelper


def host_config_serializer(host_ip):  # 第5.2步：提取给定IP的客户端主机的配置信息
    applied_services = []
    configs = {
        "services": {},
        # "refresh_config_interval":
    }

    for group in hosts.monitored_groups:
        if host_ip in group.hosts:
            applied_services.extend(group.services)
    # print(applied_services)
    applied_services = set(applied_services)
    # print(applied_services)

    for service in applied_services:
        service = service()
        configs["services"][service.name] = [service.interval, service.plugin_name, 0]

    return configs


# # 不可用
# def all_host_configs():
#     applied_hosts = []
#     for group in hosts.monitored_groups:
#         applied_hosts.extend(group.hosts)
#     applied_hosts = set(applied_hosts)
#
#     for host_ip in applied_hosts:
#         host_config = host_config_serializer(host_ip)
#         print(host_config)
#
#
# def get_host_configs(server_instance, msg):
#     ipaddr = msg.get("ip")
#     print("get here...")
#     congifs = host_config_serializer(ipaddr)
#     server_instance.redis.set(ipaddr, pickle.dumps(congifs))

# # 可用
# def all_hosts_configs():
#     all_hosts_ip = []
#     hosts_configs = {}
#     hosts_configs_2 = {}
#     for group in hosts.monitored_groups:
#         all_hosts_ip.extend(group.hosts)
#     all_hosts_ip = list(set(all_hosts_ip))
#     for host_ip in all_hosts_ip:
#         hosts_configs[host_ip] = host_config_serializer(host_ip)["services"]
#     hosts_configs_2["hosts"] = hosts_configs
#     return hosts_configs_2


def all_hosts_configs():
    configs = {"hosts": {}}
    for group in hosts.monitored_groups:
        for host_ip in group.hosts:
            # if host_ip not in configs["hosts"]:
            configs["hosts"][host_ip] = {}

    return configs


def flush_all_hosts_configs_into_redis():  # 第5步：将客户端配置信息装入redis
    applied_hosts = []
    redis = RedisHelper()

    # 第5.1步：从hosts.monitored_groups载入客户端主机配置模板，group是不同的templates的实例化；
    # group的字段有：name, group_name, hosts, services；
    # group.hosts是该group的所有客户端主机IP地址的list；
    # group.services是该group的所有services的list, list内容为不同客户端主机机型（如windows、linux）、不同监控项目（如cpu、memory）所要监控的指标的class
    for group in hosts.monitored_groups:
        applied_hosts.extend(group.hosts)  # 将所有客户端主机IP地址的list合并成一个list
    applied_hosts = set(applied_hosts)

    for host_ip in applied_hosts:
        host_config = host_config_serializer(host_ip)  # 第5.2步：提取给定IP的客户端主机的配置信息
        key = "HostConfig::%s" % host_ip
        redis.set(key, pickle.dumps(host_config))  # 第5.3步：将给定IP的客户端主机的配置信息按照（key, value）格式装入redis

    return True


def report_service_data(server_instance, msg):
    host_ip = msg["ip"]
    service_status_data = msg["data"]
    service_name = msg["service_name"]

    server_instance.hosts["hosts"][host_ip][service_name] = {
        "data": service_status_data,
        "time_stamp": time.time()
    }
    key = "StatusData::%s" % host_ip
    server_instance.redis.set(key, pickle.dumps(server_instance.hosts["hosts"]))


if __name__ == "__main__":
    # host_config_serializer("10.165.13.233")
    # flush_all_hosts_configs_into_redis()
    pass
