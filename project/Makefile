FRONT_END_BINARY=frontApp
BROKER_BINARY=brokerApp
AUTH_BINARY=authApp
LOGGER_BINARY=loggerServiceApp
MAIL_BINARY=mailerApp
LISTENER_BINARY=listenerApp

## up: starts all containers in the background without forcing build
up:
	@echo "Starting Docker images..."
	docker-compose up -d
	@echo "Docker images started!"

## up_build: stops docker-compose (if running), builds all projects and starts docker compose
up_build: build_broker build_logger build_auth build_mail build_listener
	@echo "Stopping docker images (if running...)"
	docker-compose down
	@echo "Building (when required) and starting docker images..."
	docker-compose up --build -d
	@echo "Docker images built and started!"

## down: stop docker compose
down:
	@echo "Stopping docker compose..."
	docker-compose down
	@echo "Done!"

## build_broker: builds the broker binary as a linux executable
build_broker:
	@echo "1.Building broker binary..."
	cd ../broker-service && env GOOS=linux CGO_ENABLED=0 go build -o ${BROKER_BINARY} ./cmd/api
	@echo "Done!"

## build_logger: builds the logger binary as a linux executable
build_logger:
	@echo "2.Building logger binary..."
	cd ../logger-service && env GOOS=linux CGO_ENABLED=0 go build -o ${LOGGER_BINARY} ./cmd/api
	@echo "Done!"

## build_auth: builds the auth binary as a linux executable
build_auth:
	@echo "3.Building auth binary..."
	cd ../authentication-service && env GOOS=linux CGO_ENABLED=0 go build -o ${AUTH_BINARY} ./cmd/api
	@echo "Done!"

## build_mail: builds the mail binary as a linux executable
build_mail:
	@echo "4.Building mail binary..."
	cd ../mail-service && env GOOS=linux CGO_ENABLED=0 go build -o ${MAIL_BINARY} ./cmd/api
	@echo "Done!"

## build_listener: builds the listener binary as a linux executable
build_listener:
	@echo "5.Building listener binary..."
	cd ../listener-service && env GOOS=linux CGO_ENABLED=0 go build -o ${LISTENER_BINARY} .
	@echo "Done!"

## build_front: builds the frone end binary
build_front:
	@echo "Building front-end binary..."
	cd ../front-end && env CGO_ENABLED=0 go build -o ${FRONT_END_BINARY} ./cmd/web
	@echo "Done!"

## start: starts the front end
start: build_front
	@echo "Starting front end"
	cd ../front-end && ./${FRONT_END_BINARY} &

## stop: stop the front end
stop:
	@echo "Stopping front end..."
	@-pkill -SIGTERM -f "./${FRONT_END_BINARY}"
	@echo "Stopped front end!"

authName=authentication-service
brokerName=broker-service
listenerName=listener-service
loggerName=logger-service
mailName=mail-service
# docker build -f ./service.dockerfile -t cstungthanh/${mailName}:0.1.0 .
build_images:
	cd ../${authName} && docker build -f ./${authName}.dockerfile -t cstungthanh/${authName}:0.1.0 .
	cd ../${brokerName} && docker build -f ./${brokerName}.dockerfile -t cstungthanh/${brokerName}:0.1.0 .
	cd ../${listenerName} && docker build -f ./${listenerName}.dockerfile -t cstungthanh/${listenerName}:0.1.0 .
	cd ../${loggerName} && docker build -f ./${loggerName}.dockerfile -t cstungthanh/${loggerName}:0.1.0 .
	cd ../${mailName} && docker build -f ./${mailName}.dockerfile -t cstungthanh/${mailName}:0.1.0 .

push_images:
	docker push cstungthanh/${authName}:0.1.0
	docker push cstungthanh/${brokerName}:0.1.0
	docker push cstungthanh/${listenerName}:0.1.0
	docker push cstungthanh/${loggerName}:0.1.0
	docker push cstungthanh/${mailName}:0.1.0

start_postgres:
	docker-compose -f ./postgres.yml up -d