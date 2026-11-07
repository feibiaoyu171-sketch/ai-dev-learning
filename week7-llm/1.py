import requests
import math
from config import DEEPSEEK_API_KEY,Embedding_Key

def chat(messages):
    r = requests.post("https://api.deepseek.com/v1/chat/completions",
                      headers={"Authorization":f"Bearer {DEEPSEEK_API_KEY}"},
                      json={"model":"deepseek-chat","messages":messages})
    return r.json()["choices"][0]["message"]["content"]

def embed(text):
    r = requests.post("https://api.siliconflow.cn/v1/embeddings",
                      headers={"Authorization":f"Bearer {Embedding_Key}"},
                      json={"model":"BAAI/bge-large-zh-v1.5","input":text})

    return r.json()["data"][0]["embedding"]

def cos_sim(a,b):
    dot = 0
    na = 0
    nb = 0
    for i in range(len(a)):
        dot += a[i] * b[i]
        na += a[i] * a[i]
        nb += b[i] * b[i]
    return dot / (math.sqrt(na) * math.sqrt(nb))

documents = [
    "SAR（合成孔径雷达）水深反演是利用卫星 SAR 影像反演浅海水深的技术。",
    "它主要适用于 20-100 米的浅水区域。",
    "常用方法包括波浪频散法、极化比法等。",
    "研究区通常选择海南岛、西沙群岛等南海海域。",
]

doc_vectors = []
for doc in documents:
    doc_vectors.append((doc,embed(doc)))

question = "SAR 水深反演适合多深的水域？"
que_vec = embed(question)
scores = []
for doc,vec in doc_vectors:
    scores.append((cos_sim(vec,que_vec),doc))
scores.sort(reverse=True)

top2 = []
for item in scores[:2]:
    top2.append(item[1])

answer = chat([{"role":"system","content":"你根据提供的资料回答，资料里没有的就说不知道，不要编造"},{"role":"user","content":"资料:"+"\n".join(top2)+"问题："+question}])
print("检索到的资料：", top2)
print("AI 回答：", answer)


