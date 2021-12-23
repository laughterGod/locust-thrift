# -*- coding: utf-8 -*-
"""
# 该文件仅仅是用于模拟待压测服务使用的。
# 正式压测过程中可以忽略该文件。
"""
import thriftpy
from thriftpy.rpc import make_server
import os
from settings import ROOT_PATH

eb_thrift = thriftpy.load(os.path.join(ROOT_PATH, "thrift_file/eb.thrift"), module_name="eb_thrift")


class Dispatcher(object):
    def batch_route_eta_broker_rb_pack(self):
        return "eb case success~~"


server = make_server(eb_thrift.didi_eta, Dispatcher(), '127.0.0.1', 6000)
server.serve()
