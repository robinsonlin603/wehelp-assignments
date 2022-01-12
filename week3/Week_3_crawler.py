import urllib.request as req
import json
url="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with req.urlopen(url) as response:
    data=json.load(response)
datas=data["result"]["results"]
with open("week3\data.csv","w",encoding="utf-8") as file:
    for list in datas:
        dist=list["address"][5:8]
        pics=list["file"].split("https")
        pic="https"+pics[1].lower()
        file.write(list["stitle"]+","+dist+","+list["longitude"]+","+list["latitude"]+","+pic+"\n")