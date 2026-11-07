import requests
from config import DEEPSEEK_API_KEY


def chat(prompt):
    """给 DeepSeek 发一句话，返回它的回答"""
    r = requests.post(
        "https://api.deepseek.com/v1/chat/completions",
        headers={"Authorization": f"Bearer {DEEPSEEK_API_KEY}"},
        json={
            "model": "deepseek-chat",
            "messages": [{"role": "user", "content": prompt}]
        }
    )
    return r.json()["choices"][0]["message"]["content"]


print(chat("你好，介绍一下你自己"))
