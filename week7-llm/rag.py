"""第一个真 RAG：检索增强生成"""
import math
import requests
from config import DEEPSEEK_API_KEY, Embedding_Key


def embed(text):
    """把文字转成向量（embedding）"""
    r = requests.post(
        "https://api.siliconflow.cn/v1/embeddings",
        headers={"Authorization": f"Bearer {Embedding_Key}"},
        json={"model": "BAAI/bge-large-zh-v1.5", "input": text}
    )
    return r.json()["data"][0]["embedding"]


def cos_sim(a, b):
    """余弦相似度：越接近 1 越相似"""
    dot = 0
    na = 0
    nb = 0
    for i in range(len(a)):
        dot += a[i] * b[i]
        na += a[i] * a[i]
        nb += b[i] * b[i]
    return dot / (math.sqrt(na) * math.sqrt(nb))


def chat(messages):
    r = requests.post(
        "https://api.deepseek.com/v1/chat/completions",
        headers={"Authorization": f"Bearer {DEEPSEEK_API_KEY}"},
        json={"model": "deepseek-chat", "messages": messages}
    )
    return r.json()["choices"][0]["message"]["content"]


# ① 资料，切成几段
documents = [
    "SAR（合成孔径雷达）水深反演是利用卫星 SAR 影像反演浅海水深的技术。",
    "它主要适用于 20-100 米的浅水区域。",
    "常用方法包括波浪频散法、极化比法等。",
    "研究区通常选择海南岛、西沙群岛等南海海域。",
]

# ② 每段转成向量
doc_vectors = []
for doc in documents:
    doc_vectors.append((doc, embed(doc)))

# ③ 提问，转成向量
question = "SAR 水深反演适合多深的水域？"
q_vec = embed(question)

# ④ 找最相近的 2 段
scores = []
for doc, vec in doc_vectors:
    scores.append((cos_sim(q_vec, vec), doc))
scores.sort(reverse=True)          # 相似度从高到低排
top2 = [doc for _, doc in scores[:2]]

# ⑤ 塞进 prompt，生成回答
answer = chat([
    {"role": "system", "content": "你根据提供的资料回答，资料里没有的就说不知道，不要编造"},
    {"role": "user", "content": "资料：\n" + "\n".join(top2) + "\n\n问题：" + question}
])
print("检索到的资料：", top2)
print("AI 回答：", answer)
