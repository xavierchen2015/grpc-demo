from concurrent import futures
import time

import grpc

import demo_pb2
import demo_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class demo_service(demo_pb2_grpc.demoapiServicer):
    def sayhello(self, request, context):

        new_customer = []
        new_member = demo_pb2.Member()
        new_member2 = demo_pb2.Member()

        new_member.uid = 11
        new_member.name = "xx"
        new_member.email = "xx@gmail.com"

        phone = new_member.phones.add()

        phone.number = "0988000999"

        new_member2.uid = 22
        new_member2.name = "xx"
        new_member2.email = "xx@gmail.com"

        phone2 = new_member2.phones.add()

        phone2.number = "1111111111"
        phone2.type = demo_pb2.Member.MOBILE

        new_customer.append(new_member)
        new_customer.append(new_member2)
        
        return demo_pb2.Customers(member=new_customer)
        
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    demo_pb2_grpc.add_demoapiServicer_to_server(demo_service(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()