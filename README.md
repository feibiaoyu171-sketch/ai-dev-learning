# AI 应用开发学习计划

方向：大模型应用（LLM / RAG / Agent）。完整技术栈分四层，这份目录先打第一层。

## 第一层：工程地基（Python + MySQL + FastAPI + Docker）

这一层是后面所有内容的前提，缺了它会学得很吃力。目标不是「从零学 Python」，而是把你现在的科研脚本能力升级成工程能力。

- 时长：约 6 周，每周 10~20 小时
- 方式：项目驱动，每周围绕一个小项目展开
- 产出：6 周后能独立做出一个「数据库 → API → Docker 一键部署」的完整小应用

## 总原则

1. 每周围绕一个小项目展开，先写后查（写不动了再看教程）。
2. 全程用 Git，每个小项目都推到 GitHub。
3. 项目例子统一用「水深 / 海洋数据」主题，贴合 SAR 水深课题；数据用假数据即可，不碰真实 GEBCO/Sentinel 数据。
4. 每周结尾在「学习小结」里写几段本周收获 + 卡点，月末汇总。

## 周计划

### 第 1 周：环境 + Python 复习补缺 + Git
- 环境：VS Code + Python + conda（或 venv）虚拟环境；搞清楚「为什么要有虚拟环境」
- Python 快速复习：变量/类型、条件/循环、函数、list/dict
- 模块与包、pip 装第三方库、写 requirements.txt
- Git：init / add / commit / push，建 GitHub 仓库
- 小项目：写一个命令行小工具，读水深采样点 CSV，算最大值/最小值/平均值

### 第 2 周：面向对象 + 异常处理 + 文件数据
- 类、对象、`__init__`、继承
- 异常处理 try/except，什么时候用
- 常用库：pathlib、json、csv、requests
- 小项目：把第 1 周工具用面向对象重构，支持读 CSV 和 JSON 两种格式

### 第 3 周：MySQL
- 安装 MySQL；库、表、行、列、主键
- SQL：CREATE TABLE、INSERT、SELECT、UPDATE、DELETE、WHERE、ORDER BY、LIMIT
- 小项目：建「水深测量点」数据库，手动建表、插入假数据、写查询

### 第 4 周：Python 连 MySQL + FastAPI 起步
- pymysql（或 SQLAlchemy）连数据库
- HTTP 基础：GET/POST、URL、查询参数、JSON、状态码
- FastAPI：第一个接口、路由、路径参数、返回 JSON
- 小项目：写接口 `/points` 返回数据库里所有水深测量点

### 第 5 周：FastAPI 完整 CRUD + 数据校验
- Pydantic 数据校验；POST 提交数据、请求体
- 完整 CRUD 接口
- 小项目：水深数据 CRUD API——新增点、查点、改点、删点，数据落到 MySQL

### 第 6 周：Docker + 综合收尾
- Docker：镜像、容器、Dockerfile、docker-compose
- 把 FastAPI + MySQL 一起打包，`docker compose up` 一键跑
- 小项目：把第 5 周 API 完整打包，别人拿到代码一条命令就能跑

## 参考资料（中文优先）

- Python：《Python编程：从入门到实践》后半部分 / 廖雪峰 Python 教程
- SQL：菜鸟教程 SQL / 廖雪峰 SQL 教程
- FastAPI：FastAPI 官方中文文档（fastapi.tiangolo.com/zh）
- Docker：阮一峰《Docker 入门教程》/ Docker 官方 Getting Started
- Git：廖雪峰 Git 教程

## 怎么算学到位

- 每周末：小项目能跑通 + 代码推到 GitHub + 学习小结写一段收获
- 月末：汇总成「学习小结」，对照 6 周目标自查进度
