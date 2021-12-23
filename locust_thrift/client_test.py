import thriftpy
eb_thrift = thriftpy.load(os.path.join(ROOT_PATH, "thrift_file/eb.thrift"), module_name="eb_thrift")

from thriftpy.rpc import make_client

client = make_client(eb_thrift.didi_eta, '127.0.0.1', 6000)
print(client.batch_route_eta_broker_rb_pack())
