#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     index
 IDE：    PyCharm
创建时间： 2019/6/3 10:12
@author： skymoon
"""

from wsgiref.simple_server import make_server


# def RunServer(environ, start_response):
#     start_response("200 OK", [('Content-Type', 'text/html')])
#
#
#     userUrl = environ["PATH_INFO"]
#
#     for item in conf.url:
#         if item[0] == userUrl:
#             return item[1]()
#     else:
#         return "404"
#
#
# if __name__ == "__main__":
#     httpd = make_server('', 8000, RunServer)
#     print("Server HTTP on port 8000...")
#     httpd.serve_forever()


def index():
    return 'index'.encode('utf-8')


def login():
    return 'login'.encode('utf-8')


def routers():
    urlpatterns = (
        ('/index/', index),
        ('/login/', login),
    )

    return urlpatterns


def RunServer(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    url = environ['PATH_INFO']
    urlpatterns = routers()
    func = None
    for item in urlpatterns:
        if item[0] == url:
            func = item[1]
            break
    if func:
        return func()
    else:
        return '404 not found'.encode('utf-8')


if __name__ == '__main__':
    httpd = make_server('', 8000, RunServer)
    print("Serving HTTP on port 8000...")
    httpd.serve_forever()
