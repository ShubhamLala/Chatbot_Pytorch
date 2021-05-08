import json
import re
with open("D:\\p\\nlp\\csvjson.json",encoding="utf8") as f:
    data=json.load(f)
rows=len(data)
for i in range(rows):
    if(type(data[i]["patterns"])==str):
        t=re.sub(r'\\u....',"'",data[i]["patterns"])
        t1=re.split("[\n]+[\\.]+|[\n]+",t)
        n1=len(t1)
        for j in range(n1):
            t1[j]=t1[j].strip() 
        while("" in t1):
            t1.remove("")
        data[i]["patterns"]=t1
    if(type(data[i]["responses"])==str):
        t=re.sub(r'\\u....',"'",data[i]["responses"])  #not working idk y
        t1=re.split("[\n]+[\\.]+|[\n]+",t)
        n1=len(t1)
        for j in range(n1):
            t1[j]=t1[j].strip() 
        while("" in t1):
            t1.remove("")
        data[i]["responses"]=t1


out_file=open("D:\\p\\nlp\\test.json","w")
json.dump(data,out_file,indent=4)
out_file.close()
