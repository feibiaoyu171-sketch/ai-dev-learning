# 第 5 周：CRUD + 数据校验

这周把接口从「只能查」升级成「增删改查全齐」。

**注意**：第 5 周的 CRUD 代码（POST / PUT / DELETE + Pydantic 校验）都在 `week4-fastapi/main.py` 里——因为跟第 4 周是同一个 FastAPI 应用，接口都写在那个文件。

## 学的东西

- HTTP 方法：GET 查、POST 增、PUT 改、DELETE 删
- Pydantic `BaseModel`：定义数据结构 + 自动校验（非法数据返回 422）
- 路径参数 `{point_id}`、`%s` 占位符、`conn.commit()`（写操作必须）

## 6 道综合复习题

1. `analyze_points(points)` —— 字典列表统计，返回 count / avg / deepest（擂主法）
2. `DataReader` 类 —— 读文件 + try/except（文件不存在返回 []）
3. SQL 三道小题 —— WHERE / ORDER BY / LIMIT / DELETE
4. `/points/filter` —— 查询参数 `?min_depth=10`
5. POST 加业务校验 —— depth_m 不能为负数
6. `/points/above/{depth}` —— 路径参数 + 过滤

做题时把每道存成 `题X.py` 放这个文件夹里，方便以后翻。
