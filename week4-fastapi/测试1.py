import requests

r1 = requests.get("http://127.0.0.1:8000/points")
print(r1.status_code)   # 200 表示成功
print(r1.json())        # 返回的 JSON，就是你的水深数据

r2 = requests.get("http://127.0.0.1:8000/points/filter",params={"min_depth":10})
print(r2.status_code)
print(r2.json())

r3 = requests.post("http://127.0.0.1:8000/points",json={"lon": 111.5, "lat": 20.6, "depth_m": 18.0, "obs_date": "2026-08-05"})
print(r3.status_code)
print(r3.json())

r4 = requests.get("http://127.0.0.1:8000/points")
if r4.status_code == 200:
    data = r4.json()
    print("成功，拿到",len(data),"条数据")

else:
    print("出错了，状态码:", r4.status_code)