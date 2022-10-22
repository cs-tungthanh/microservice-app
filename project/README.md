# Kubernetes tutorial

minikube start --nodes=2

minikube delete
minikube stop

minikube status

kubectl get pods
// pod is a basic unit in a Kubernetes cluster
// a pod can have one or more containers

// get log: name get from get pods
--> kubectl logs name

// get services
kubectl get svc  
+ kubectl delete svc broker-service

kubectl get deployment  

// run file yml
kubectl apply -f k8s
kubectl apply -f k8s/mongo.yml


- load balance
kubectl expose deployment broker-service --type=LoadBalancer --port=8080 --target-port=8080
minikube tunnel

