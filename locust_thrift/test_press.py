# -*- coding: utf-8 -*-

from locust import task, HttpUser, TaskSet
import thriftpy
from settings import ROOT_PATH
from utils import gen_loop_csv_reader
from client import RpcClient
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
        resp = self.eb_client.batch_route_eta_broker_rb_pack()
        print(resp)


class ApiEB(HttpUser):
    tasks = [TestPress]
    stop_timeout = None
    min_wait = 0
    max_wait = 0

if __name__ == "__main__":
    os.system("locust -f ./test_press.py --web-host=10.96.114.24 --host=https://www.baidu.com")


