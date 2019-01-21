### Prepare 

- golang environment
- python environment

### Install
- Package for gRPC Python. [https://github.com/grpc/grpc/tree/master/src/python/grpcio](https://github.com/grpc/grpc/tree/master/src/python/grpcio)

```
python -m pip install grpcio
```

- protocol buffer compiler tools
```
python -m pip install grpcio-tools
```

- 同時會用 golang 來寫測試，所以一起安裝
```
go get -u github.com/golang/protobuf/{proto,protoc-gen-go}
```

### Code

#### demo.proto
- compiler

  python
  ```
  python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./member.proto
  ```
  get 
  - demo_pb2.py
  - demo_pb2_grpc.py
  
  go
  ```
  protoc --go_out=plugins=grpc:./pb *.proto
  ```
  get 
  - demo.pb.go

#### server
  - start
  ```
  python3 server.py
  ```

#### client
  - py
  ```
  python3 client.py
  ```
  - go
  ```
  go run client.go
  ```

