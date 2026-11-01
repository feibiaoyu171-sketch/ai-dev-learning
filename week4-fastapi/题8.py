from fastapi import FastAPI
import pymysql
from statsmodels.graphics.tukeyplot import results

app = FastAPI()
@app.get("/deepest")
def get_deepest():
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="1712971580wdsj!",
        database="bathymetry"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM points ORDER BY depth_m DESC LIMIT 1")
    row = cursor.fetchone()
    conn.close()
    return {
        "id": row[0],
        "lon": row[1],
        "lat": row[2],
        "depth_m": row[3],
        "obs_date": str(row[4])
    }
