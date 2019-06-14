#!/usr/bin/env python
# -*- coding:utf-8 -*-


from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.


@api_view(['GET', 'PUT', 'POST', 'DELETE'])
def receive_server_info(request):
    server_info = request.POST.get("data")
    print(server_info)
    print(type(server_info))
    # server_info_dict = json.loads(server_info)
    # print(server_info_dict)
    return Response('ok')


def install_os(request):
    pass


@api_view(['GET', 'PUT', 'POST', 'DELETE'])
def servers(request):
    method = request.method

    if method == 'POST':
        pass

    return Response('dddd')
