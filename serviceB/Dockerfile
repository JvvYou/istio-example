# 使用官方 Python 基础镜像，选择适合项目的版本
FROM python:3.11.10

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

ENV SW_AGENT_COLLECTOR_BACKEND_SERVICES=tracing.istio-system.svc.cluster.local:11800 SW_AGENT_NAME=service-b-c-agent SW_AGENT_INSTANCE_NAME=service-b-c-instance

COPY . .

EXPOSE 9000

CMD ["sw-python", "run", "-p", "gunicorn", "app.main:app", "--workers", "2", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:9000"]


