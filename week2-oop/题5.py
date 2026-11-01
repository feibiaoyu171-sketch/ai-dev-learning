def safe_get(d, key):
    try:
        return d[key]

    except KeyError:
        return None

print(safe_get({"a":1}, "b"))