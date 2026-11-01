from fontTools.misc.cython import returns

d = {"a": 1, "b": 2}
def get_value(name,d):
    try:
        return d[name]
    except KeyError:
        return "键不存在"
print(get_value("c",d))