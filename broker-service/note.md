- init project: go mod init broker

- cmd/api/main.go: main entry of broker service

- install go-chi
go get github.com/go-chi/chi/v5
go get github.com/go-chi/chi/v5/middleware
go get github.com/go-chi/cors

do something with it and then respond saying yeah, I've got the response
I just want to make sure that I can connect from the FE to the broker service.
overtime, the broker will become much more complex so I just going to do one thing.
Broker service: It's going to take requests and forward them off to some microservice and then send a response back.

Sep 13:
- init front-end
- init broker-service: setup get request and response through http
- create docker to build broker-service

what we're going to do to start with is set up a type
and anytime you want to implement in our PC sever, you do need a specific type of that
and it doesn't have to have any particular magic about it
just declare it type and I'll call our PC server and it's a struct and it has no members at all.

we're also going to want to define the kind of payload that we're going to receive from our PC

here something I'm going to expose