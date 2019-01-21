import grpc

import demo_pb2
import demo_pb2_grpc

from __future__ import print_function
from google.protobuf import json_format

def run():
    with grpc.insecure_channel('127.0.0.1:50051') as channel:
        stub = demo_pb2_grpc.demoapiStub(channel)
        response = stub.sayhello(demo_pb2.empty_request())
    
        new = demo_pb2.Customers()

    print(json_format.MessageToJson(response, True))

if __name__ == '__main__':
    run()
