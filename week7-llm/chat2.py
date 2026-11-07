import requests
from config import DEEPSEEK_API_KEY
def chat(messages):
    r = requests.post("https://api.deepseek.com/v1/chat/completions",
                      headers={"Authorization":f"Bearer {DEEPSEEK_API_KEY}"},
                      json={"model":"deepseek-chat",
                            "messages":messages})
    return r.json()["choices"][0]["message"]["content"]
资料 = """
SAR（合成孔径雷达）水深反演是利用卫星 SAR 影像反演浅海水深的技术。
它主要适用于 20-100 米的浅水区域，依赖海浪在 SAR 影像上的成像特征。
常用方法包括波浪频散法、极化比法等。
"""
history = [{"role":"system","content": f"你根据提供的资料回答用户问题，资料里没有的就说不知道，不要编造,资料如下 {资料} "}]

while True:
    user_input = input("你:")
    if user_input == "退出" :
        break
    history.append({"role":"user","content":user_input})
    reply = chat(history)
    history.append({"role":"assistant","content":reply})
    print("AI:",reply)

