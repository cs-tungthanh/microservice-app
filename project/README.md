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

kubectl get deployment  

// run file yml
kubectl apply -f k8s
kubectl apply -f k8s/mongo.yml
