## 项目说明
基于Locust和thriftpy扩展的用于thrift协议的压测工具。

Step1：下载/拉取代码库
```
git clone https://github.com/laughterGod/locust-thrift.git
```

Step2：安装相关依赖库
```
pip install -r requirements.txt
```

Step3：启动模拟待测服务（演示时使用，正常压测其他待测服务时，无需启动Server）
```
python3 server.py
```

Step4：启动Locust压测服务：
```
python3 test_press.py
```

Step5：打开浏览器，访问http://ip:8089/
例如：http://10.96.114.24:8089/

输入并发数目和每秒启动并发数后，即正常开始压测。

Ps：那么我们应该如何对一个新的待测服务进行压测呢？
主要是编写test_press.py即可

