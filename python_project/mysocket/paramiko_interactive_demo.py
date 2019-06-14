#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     paramiko_interactive_demo.py
 IDE：    PyCharm
创建时间： 2019/5/28 12:15
@author： skymoon
"""

import socket
import sys
import time

import paramiko
from paramiko.py3compat import u

# windows does not have termios...
try:
    import termios
    import tty

    has_termios = True
except ImportError:
    has_termios = False


def interactive_shell(chan):
    if has_termios:
        posix_shell(chan)
    else:
        windows_shell(chan)


def posix_shell(chan):
    import select

    oldtty = termios.tcgetattr(sys.stdin)
    f = open("record.txt", "a+")
    try:
        tty.setraw(sys.stdin.fileno())
        tty.setcbreak(sys.stdin.fileno())
        chan.settimeout(0.0)
        records = []

        while True:
            r, w, e = select.select([chan, sys.stdin], [], [])
            if chan in r:
                try:
                    x = u(chan.recv(1024))
                    if len(x) == 0:
                        print("\r\n*** EOF\r\n")
                        break
                    sys.stdout.write(x)
                    sys.stdout.flush()
                except socket.timeout:
                    pass
            if sys.stdin in r:
                x = sys.stdin.read(1)
                records.append(x)
                if x == "\r":
                    c_time = time.strftime("%Y-%m-%d %H:%M:%S")
                    cmd = "".join(records).replace("\r", "\n")
                    log = "%s    %s" % (c_time, cmd)
                    f.write(log)
                    records = []
                if len(x) == 0:
                    break
                chan.send(x)
            # print(records)
        # print(records)

    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, oldtty)
        f.close()


# thanks to Mike Looijmans for this code
def windows_shell(chan):
    import threading

    sys.stdout.write(
        "Line-buffered terminal emulation. Press F6 or ^Z to send EOF.\r\n\r\n"
    )
    records = []

    def writeall(sock):
        while True:
            data = sock.recv(256)
            if not data:
                sys.stdout.write("\r\n*** EOF ***\r\n\r\n")
                sys.stdout.flush()
                break
            sys.stdout.write(data)
            sys.stdout.flush()

    writer = threading.Thread(target=writeall, args=(chan,))
    writer.start()

    try:
        while True:
            d = sys.stdin.read(1)
            if not d:
                break

            if d == "\r":
                records.append(d)
                c_time = time.strftime("%Y-%m-%d %H:%M:%S")
                cmd = "".join(records).replace("\r", "\n")
                log = "%s    %s" % (c_time, cmd)
                sys.stdout.write(log)
                records = []

            chan.send(d)
    except EOFError:
        # user hit ^Z or F6
        pass


if __name__ == "__main__":
    trans = paramiko.Transport(('192.168.1.102', 8088))
    trans.start_client()
    trans.auth_password(username='skymoon', password='skymoon666')
    channel = trans.open_session()
    channel.get_pty()
    channel.invoke_shell()
