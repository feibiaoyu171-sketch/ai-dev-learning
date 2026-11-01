-- 第 3 周 MySQL 练习
-- 连法：cd 到 MySQL bin 目录，跑 mysql -u root -p，输密码
-- 注意：每条 SQL 都要以分号 ; 结尾

-- 看有哪些数据库
SHOW DATABASES;

-- 建水深数据库
CREATE DATABASE bathymetry;

-- 进入这个库
USE bathymetry;

-- 建测量点表（id 主键、自动递增）
CREATE TABLE points (
    id INT PRIMARY KEY AUTO_INCREMENT,
    lon DOUBLE,
    lat DOUBLE,
    depth_m DOUBLE,
    obs_date DATE
);

-- 查看表结构
DESC points;

-- 插入数据（数字不加引号，字符串/日期加单引号）
INSERT INTO points (lon, lat, depth_m, obs_date) VALUES
(110.62, 20.18, 8.5, '2026-08-01'),
(110.75, 20.22, 15.2, '2026-08-01'),
(110.88, 20.30, 23.7, '2026-08-01');

-- 查询所有（* 表示所有列）
SELECT * FROM points;

-- 条件查询 WHERE
SELECT * FROM points WHERE depth_m > 20;
SELECT * FROM points WHERE depth_m <= 15;
SELECT * FROM points WHERE lon > 110.7 AND depth_m < 20;
SELECT * FROM points WHERE depth_m BETWEEN 10 AND 30;

-- 排序 ORDER BY（DESC 表示从大到小）
SELECT * FROM points ORDER BY depth_m;
SELECT * FROM points ORDER BY depth_m DESC;

-- 只取前几条 LIMIT
SELECT * FROM points ORDER BY depth_m DESC LIMIT 1;

-- 修改数据（WHERE 不能忘！忘了会改掉所有行）
UPDATE points SET depth_m = 25.0 WHERE id = 3;

-- 删除数据（WHERE 不能忘！忘了会清空整张表）
DELETE FROM points WHERE id = 3;

-- 聚合统计
SELECT COUNT(*) FROM points;      -- 有几行
SELECT AVG(depth_m) FROM points;  -- 平均水深
SELECT MAX(depth_m) FROM points;  -- 最大水深
SELECT MIN(depth_m) FROM points;  -- 最小水深
SELECT SUM(depth_m) FROM points;  -- 总和
