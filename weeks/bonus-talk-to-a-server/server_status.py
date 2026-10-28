# server_status.py: ask a Minecraft server who's online

import json
import urllib.request

server = "mc.hypixel.net"  # change this to your own server's address

url = "https://api.mcsrvstat.us/3/" + server
request = urllib.request.Request(url, headers={"User-Agent": "dungeon-quests"})
response = urllib.request.urlopen(request)
data = json.loads(response.read())

if data["online"]:
    print(server, "is online!")
    print("Players:", data["players"]["online"], "out of", data["players"]["max"])
else:
    print(server, "is offline.")
