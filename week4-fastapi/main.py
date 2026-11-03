from fastapi import FastAPI
import pymysql
from config import MYSQL_PASSWORD
from pydantic import BaseModel
app = FastAPI()


@app.get("/points")
def get_points():
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password=MYSQL_PASSWORD,
        database="bathymetry"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM points")
    rows = cursor.fetchall()
    conn.close()
    results = []
    for row in rows:
        results.append(
            {"id": row[0], "lon": row[1], "lat": row[2], "depth_m": row[3], "obs_date": str(row[4])}
        )
    return results


@app.get("/deepest")
def get_deepest():
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password=MYSQL_PASSWORD,
        database="bathymetry"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM points ORDER BY depth_m DESC LIMIT 1")
    row = cursor.fetchone()
    conn.close()
    return {"id": row[0], "lon": row[1], "lat": row[2], "depth_m": row[3], "obs_date": str(row[4])}


@app.get("/stats")
def get_stats():
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password=MYSQL_PASSWORD,
        database="bathymetry"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*), AVG(depth_m), MAX(depth_m), MIN(depth_m) FROM points")
    row = cursor.fetchone()
    conn.close()
    return {"count": row[0], "avg": row[1], "max": row[2], "min": row[3]}
class Point(BaseModel):
    lon:float
    lat:float
    depth_m:float
    obs_date:str
@app.post("/points")
def create_point(point: Point):
    if point.depth_m <0:
        return {"error": "水深不能为负数"}
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password=MYSQL_PASSWORD,
        database="bathymetry"
    )
    cursor = conn.cursor()
    cursor.execute("INSERT INTO points (lon,lat,depth_m,obs_date) VALUES (%s,%s,%s,%s)" ,(point.lon,point.lat,point.depth_m,point.obs_date))
    conn.commit()
    conn.close()
    return {"message":"已成功插入"}

@app.put("/points/{point_id}")
def update_point(point_id:int,point:Point):
        conn = pymysql.connect(
            host="localhost",
            user="root",
            password=MYSQL_PASSWORD,
            database="bathymetry"
        )
        cursor = conn.cursor()
        cursor.execute("UPDATE points SET lon = %s,lat = %s,depth_m = %s,obs_date = %s WHERE id = %s",(point.lon,point.lat,point.depth_m,point.obs_date,point_id))
        conn.commit()
        conn.close()
        return {"message":"已成功修改"}

@app.delete("/points/{point_id}")
def delete_point(point_id: int):
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password=MYSQL_PASSWORD,
        database="bathymetry"
    )
    cursor = conn.cursor()
    cursor.execute("DELETE FROM points WHERE id = %s",(point_id,))
    conn.commit()
    conn.close()
    return {"message":"删除成功"}

@app.get("/points/filter")
def filter_points(min_depth:float= 0):
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password=MYSQL_PASSWORD,
        database="bathymetry"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM points WHERE depth_m>= %s",(min_depth,))
    rows = cursor.fetchall()
    conn.close()
    results = []
    for row in rows:
        results.append({"id":row[0],"lon":row[1],"lat":row[2],"depth_m":row[3],"obs_date":row[4]})
    return results

@app.get("/points/above/{depth}")
def get_depth(depth:float=0):
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password=MYSQL_PASSWORD,
        database="bathymetry"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM points WHERE depth_m > %s",(depth,))
    rows = cursor.fetchall()
    conn.close()
    results = []
    for row in rows:
        results.append({"id":row[0],"lon":row[1],"lat":row[2],"depth_m":row[3],"obs_date":row[4]})
    return results