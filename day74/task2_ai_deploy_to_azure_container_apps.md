# Day 74 · Task 2 · AI & ML: Deploy to Azure Container Apps

> Push your image to a container registry. Then: Azure Container Apps (or Cloud Run / App Runner). Then: Set environment variables and secrets in the cloud.

## Part 1: Registry

## Push the image
```
az acr create -n <registryname> -g <group> --sku Basic
az acr login -n <registryname>
docker tag my-agent <registryname>.azurecr.io/my-agent:v1
docker push <registryname>.azurecr.io/my-agent:v1
```

## Part 2: Deploy

## Deploy
```
az containerapp up -n my-agent -g <group> --image <registryname>.azurecr.io/my-agent:v1 --ingress external --target-port 8000
```
- Public URL:
- [ ] /health returns ok

## Part 3: Config

## Config in the cloud
- [ ] Secrets set as Container App secrets, not baked into the image
- [ ] Env vars reference them
- How I'd rotate a leaked key:
