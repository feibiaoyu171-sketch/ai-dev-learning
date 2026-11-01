from fastapi import FastAPI
import pymysql
from config import MYSQL_PASSWORD

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
