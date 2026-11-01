from fastapi import FastAPI
import pymysql

app = FastAPI()
@app.get("/stats")
def get():
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="1712971580wdsj!",
        database="bathymetry"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*),AVG(depth_m),MAX(depth_m),MIN(depth_m) FROM points ")
    row = cursor.fetchone()
    conn.close()
    return {"count": row[0], "avg": row[1], "max": row[2], "min": row[3]}