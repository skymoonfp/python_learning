#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     myparamiko.py
 IDE：    PyCharm
创建时间： 2019/5/27 0:30
@author： skymoon
"""

import paramiko


def ssh_():
    # private_key = paramiko.RSAKey.from_private_key_file('/home/auto/.ssh/id_rsa')  # 免密登陆

    # 创建SSH对象
    ssh = paramiko.SSHClient()

    # 把要连接的机器添加到known_hosts文件中
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # 连接服务器
    # ssh.connect(hostname="192.168.1.1", port=139, username="sh", pkey=private_key)  # 免密登陆
    ssh.connect(hostname="192.168.1.106", port=22, username="skymoon", password="skymoon666")  # 密码登陆

    cmd = 'df'
    # cmd = 'ls -l;ifconfig'  #多个命令用;隔开
    stdin, stdout, stderr = ssh.exec_command(cmd)

    result = stdout.read()
    if not result:
        result = stderr.read()
    print(result)

    ssh.close()


def sftp_():
    private_key = paramiko.RSAKey.from_private_key_file('/home/auto/.ssh/id_rsa')  # 免密登陆

    transport = paramiko.Transport(('192.168.1.96', 22))

    transport.connect(username='morra', pkey=private_key)  # 免密登陆
    # transport.connect(username='morra', password='XXXX')  # 密码登陆

    sftp = paramiko.SFTPClient.from_transport(transport)

    sftp.put('123.py', '/tmp/test.py')  # 将123.py 上传至服务器 /tmp下并改名为test.py

    sftp.get('remove_path', 'local_path')  # 将remove_path 下载到本地 local_path

    transport.close()


if __name__ == "__main__":
    ssh_()
    # sftp_()
