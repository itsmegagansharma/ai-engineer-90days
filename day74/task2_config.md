# Day 74 · Task 2: Config

> ConfigMaps and Secrets for settings and keys.

## Config & secrets
```
kubectl create secret generic agent-secrets --from-env-file=.env
kubectl create configmap agent-config --from-literal=LOG_LEVEL=info
```
- [ ] Pod reads both
