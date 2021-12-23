# -*- coding: utf-8 -*-

from locust import task, HttpUser, TaskSet
import thriftpy
from locust_thrift.settings import ROOT_PATH
from locust_thrift.utils import gen_loop_csv_reader
from locust_thrift.client import RpcClient
import os


class TestPress(TaskSet):
    # test_file = gen_loop_csv_reader('csv/test_file.csv', '|')  # 每个参数以|分割,可以自己写

    def on_start(self):
        eb_thrift = thriftpy.load(os.path.join(ROOT_PATH, "thrift_file/eb.thrift"),
                                        module_name="eb_thrift")
        self.eb_client = RpcClient(eb_thrift.didi_eta, '127.0.0.1', 6000)

    @task
    def get_batch_route_eta_broker_rb_pack(self):
        # self.test_file.next()  # 每次获取csv一行数据,可以取出放入thrift、http、socket接口中
        a = self.eb_client.batch_route_eta_broker_rb_pack()
        print(a)


class ApiPingPong(HttpUser):
    tasks = [TestPress]
    stop_timeout = None
    min_wait = 0
    max_wait = 0
