import requests
import json
#为什么之间的代码没有导入json
from config import DEEPSEEK_API_KEY

tools = [
    {
        "type":"function",
        "function":{
            "name":"query_depth",
            "description":"查询某个地点的水深",
            "parameters":{
                "type":"object",
                "properties":{
                    "location":{"type":"string","description":"地点名"}
                },"required":["location"]
            }
        }
    }
]
#解释一下这个tools这段代码，好复杂

def query_depth(location):
    data =  {"海南岛": 42.5, "西沙群岛": 58.3, "文昌近海": 23.7}
    return data.get(location,"没这个地点的数据")

#data.get 可不可以换成 data[location]

messages = [{"role":"user","content":"海南岛的水深是多少？,严格按照资料回答"}
            ]
r1 = requests.post("https://api.deepseek.com/v1/chat/completions",
                   headers={"Authorization":f"Bearer {DEEPSEEK_API_KEY}"},
                   json={"model":"deepseek-chat","messages":messages,"tools":tools})
msg1 = r1.json()["choices"][0]["message"]#这句是在干嘛，拿到什么数据
tool_call = msg1["tool_calls"][0]#没看懂,这个是个啥东西

func_name = tool_call["function"]["name"]#这又是啥
func_args = json.loads(tool_call["function"]["arguments"])

result = query_depth(func_args["location"])

messages.append(msg1)
messages.append({"role":"tool","tool_call_id":tool_call["id"],"content":str(result)})

#更看不懂了

r2 = requests.post(
    "https://api.deepseek.com/v1/chat/completions",
    headers={"Authorization": f"Bearer {DEEPSEEK_API_KEY}"},
    json={"model": "deepseek-chat", "messages": messages}
)

print("AI 最终回答:", r2.json()["choices"][0]["message"]["content"])





