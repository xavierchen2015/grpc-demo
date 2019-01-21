package main

import (
    "log"
    "time"
    "fmt"

    "golang.org/x/net/context"
    "google.golang.org/grpc"
    rpc "demo/pb"
)

const (
    address     = "localhost:50051"
)

func main() {
    // Set up a connection to the server.
    conn, err := grpc.Dial(address, grpc.WithInsecure())
    if err != nil {
        log.Fatalf("did not connect: %v", err)
    }
    defer conn.Close()
    c := rpc.NewDemoapiClient(conn)

    // Contact the server and print out its response.
    ctx, cancel := context.WithTimeout(context.Background(), time.Second)
    defer cancel()

	r, err1 := c.Sayhello(ctx, &rpc.EmptyRequest{})
    if err1 != nil {
        log.Fatalf("could not greet: %v", err1)
    }
    fmt.Println("Greeting: ", r.Member)
}
