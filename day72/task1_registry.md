# Day 72 · Task 1: Registry

> Push your image to a container registry.

## Push the image
```
az acr create -n <registryname> -g <group> --sku Basic
az acr login -n <registryname>
docker tag my-agent <registryname>.azurecr.io/my-agent:v1
docker push <registryname>.azurecr.io/my-agent:v1
```
