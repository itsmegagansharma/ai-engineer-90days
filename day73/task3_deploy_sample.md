# Day 73 · Task 3: Deploy sample

> Follow the Kubernetes basics tutorial.

## Sample app
```
kubectl create deployment hello --image=nginx
kubectl expose deployment hello --port=80 --type=NodePort
kubectl get pods,svc
```
