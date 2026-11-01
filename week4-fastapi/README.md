# 第 4 周：FastAPI + pymysql

这周把 Python 和 MySQL 连起来，写了第一个能通过网址访问的接口服务。

## 文件

- `main.py` —— 三个接口：`/points`（查全部）、`/deepest`（查最深）、`/stats`（查统计）
- `test_db.py` —— 测试 pymysql 连数据库
- `config.py` —— 数据库密码（已被 .gitignore 忽略，**别提交到 GitHub**）

## 怎么跑

1. 激活 venv
2. `cd week4-fastapi`
3. `uvicorn main:app --reload`
4. 浏览器访问 `http://127.0.0.1:8000/docs` 看所有接口

## 记住的坑

- 加接口是「追加」，别覆盖 main.py（所有接口要共存）
- 只开一个 uvicorn；改代码没生效，先杀掉旧的再重启
- 接口代码必须存进 main.py 并 Ctrl+S
- 密码放 config.py + gitignore，不提交明文
