import json
import requests


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

def query_depth(location):
    data = {"海南岛": 42.5, "西沙群岛": 58.3, "文昌近海": 23.7}
    return data.get(location,"没这个地点的数据")

messages = [{"role":"user","content":"海南岛的水深是多少"},{"role":"system","content":"严格按照资料回答"}]

r1 = requests.post("https://api.deepseek.com/v1/chat/completions",
                   headers={"Authorization":f"Bearer {DEEPSEEK_API_KEY}"},
                   json={"model":"deepseek-chat","messages":messages,"tools":tools})

msg1 = r1.json()["choices"][0]["message"]
tool_call = msg1["tool_calls"][0]

func_name = tool_call["function"]["name"]
func_args = json.loads(tool_call["function"]["arguments"])
result = query_depth(func_args["location"])

messages.append(msg1)
messages.append({"role":"tool","tool_call_id":tool_call["id"],"content":str(result)})

r2 = requests.post("https://api.deepseek.com/v1/chat/completions",
                   headers={"Authorization":f"Bearer {DEEPSEEK_API_KEY}"},
                   json={"model":"deepseek-chat","messages":messages})
print("AI:",r2.json()["choices"][0]["message"]["content"])