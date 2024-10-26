python 3.12
kubernetes 1.30.2
istio 1.23.2

## 1、serviceA

启动serviceA
```shell
cd serviceA
pip install -r requirements.txt
fastapi run --reload app/main.py
```

构建镜像
```shell
cd serviceA

docker build -t service-a:v18 .
```

k8s部署
```shell
cd serviceA

kubectl apply -f service-a.yml
kubectl apply -f gw.yml
kubectl apply -f dr-exp.yaml
```


## 2、serviceB和serviceC

启动
```shell
cd serviceB
pip install -r requirements.txt
fastapi run --reload app/main.py --port 9000
```

构建镜像
```shell
cd serviceB

docker build -t service-b:v18 .
```
k8s部署

两个服务的镜像是同一个，区别是接口。
```shell
cd serviceB

kubectl apply -f service-b.yml
kubectl apply -f service-c.yml
```

## 3、请求
```shell
curl http://myservice-a.com/api/v1/testA/
```