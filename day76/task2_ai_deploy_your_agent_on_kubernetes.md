# Day 76 · Task 2 · AI & ML: Deploy your agent on Kubernetes

> Deployment + Service YAML for your agent. Then: ConfigMaps and Secrets for settings and keys. Then: Readiness/liveness probes, replicas; skim Helm.

## Part 1: Manifests

## deployment.yaml
```yaml
apiVersion: apps/v1
kind: Deployment
metadata: {name: my-agent}
spec:
  replicas: 2
  selector: {matchLabels: {app: my-agent}}
  template:
    metadata: {labels: {app: my-agent}}
    spec:
      containers:
        - name: api
          image: my-agent:v1
          ports: [{containerPort: 8000}]
          # TODO: envFrom secretRef, readinessProbe on /health
---
# TODO: a Service of type NodePort or LoadBalancer pointing at port 8000
```
Load a local image into kind: `kind load docker-image my-agent:v1 --name dev`

## Part 2: Config

## Config & secrets
```
kubectl create secret generic agent-secrets --from-env-file=.env
kubectl create configmap agent-config --from-literal=LOG_LEVEL=info
```
- [ ] Pod reads both

## Part 3: Scale and health

## Scale and health
- `kubectl scale deployment my-agent --replicas=3`
- Readiness vs liveness probe (one line each):
- What Helm adds:
