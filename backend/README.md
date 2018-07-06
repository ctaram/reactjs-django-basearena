Django Backend for Todo Application
===

## Deployment Instruction

#### 1. Build the image

```
docker build . --tag todo-back
```

#### 2. Spin up a container with

```
docker run -p 8000:8000 --rm todo-back
```

#### 3. Experiance Awesomeness

at [Swagger Docs](http://localhost:8000/docs/)


--
