# Day 74 · Task 1: Manifests

> Deployment + Service YAML for your agent.

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
