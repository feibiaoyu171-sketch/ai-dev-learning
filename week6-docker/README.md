# 第 6 周：Docker

这周学 Docker，把 FastAPI 应用打包成镜像、跑成容器。

## 核心比喻

**容器 = 一台独立的「小电脑」**（有自己的系统、文件、localhost、端口，跟真电脑互不相通）。

一条主线：

```
Dockerfile（说明书） --build--> 镜像（U盘） --run--> 容器（运行中的小电脑）
```

- 镜像 = 照说明书装好、打包成的文件系统快照（静态、只读、可复制）
- 容器 = 用镜像开起来、正在运行的小电脑（动态）
- build = 照说明书装电脑存 U盘（做一次）
- run = 用 U盘开电脑（想开几次开几次）

## Dockerfile 六行

```dockerfile
FROM python:3.13-slim                     # 起点：装好 Python 的裸机
WORKDIR /app                              # 进目录
COPY requirements.txt .                   # 放依赖清单
RUN pip install -r requirements.txt       # 装库
COPY . .                                  # 放代码
CMD ["uvicorn", "main:app", ...]          # 开机自动跑 uvicorn
```

## 两个关键参数（都源于「独立电脑」）

- `-p 8000:8000` —— 端口映射。左 = 你电脑端口，右 = 小电脑端口。因为小电脑的端口不是你电脑的端口。
- `-e DB_HOST=host.docker.internal` —— 告诉容器「数据库在宿主电脑上」。因为小电脑的 localhost 是它自己。

## 完整命令

```powershell
docker build -t my-api .          # 做镜像
docker run -e DB_HOST=host.docker.internal -p 8000:8000 my-api   # 跑容器
```

## 环境备忘

- Dockerfile 和 requirements.txt 在 `week4-fastapi/` 里（跟代码放一起）
- 装了 Docker Desktop + WSL2，配了 **DaoCloud 镜像加速器**（Docker Hub 被墙，代理方案对 build 不生效，最终用镜像源解决）
- 数据库地址改成可配置：`config.py` 里 `DB_HOST = os.environ.get("DB_HOST", "localhost")`
- 基础镜像用 `python:3.13-slim`（约 120MB，完整版约 1GB 太慢）
