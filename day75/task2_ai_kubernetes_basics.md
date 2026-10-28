# Day 75 · Task 2 · AI & ML: Kubernetes basics

> Pods, deployments, services, namespaces. Then: Install kind or minikube and kubectl. Then: Follow the Kubernetes basics tutorial.

## Part 1: Concepts

## Kubernetes words
| Term | Meaning |
|------|---------|
| Pod | |
| Deployment | |
| Service | |
| Namespace | |

## Part 2: Local cluster

```
kind create cluster --name dev
kubectl get nodes
```
- [ ] Node is Ready

## Part 3: Deploy sample

## Sample app
```
kubectl create deployment hello --image=nginx
kubectl expose deployment hello --port=80 --type=NodePort
kubectl get pods,svc
```
