def analyze_points(points):
    max_depth = 0
    total = 0
    max_name = ''
    for point in points:
        if point["depth_m"] > max_depth:
            max_depth = point["depth_m"]
            max_name = point["name"]
        total+=point["depth_m"]
    avg = total/len(points)
    return {"count": len(points), "avg":avg , "deepest": max_name}
print(analyze_points([{"name": "A站", "depth_m": 8.5}, {"name": "B站", "depth_m": 15.2}, {"name": "C站", "depth_m": 23.7}]))