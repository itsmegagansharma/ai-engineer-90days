# Day 72 · Task 2: Deploy

> Azure Container Apps (or Cloud Run / App Runner).

## Deploy
```
az containerapp up -n my-agent -g <group> --image <registryname>.azurecr.io/my-agent:v1 --ingress external --target-port 8000
```
- Public URL:
- [ ] /health returns ok
