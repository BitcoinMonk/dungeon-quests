# Bonus · Talk to a Server — Tonight's lesson

**Get there:** from the main folder, type `cd weeks/bonus-talk-to-a-server`

**Start the week:** merge last week's pull request together, then `git checkout main`, `git pull`, `git checkout -b bonus`

**Together with your mentor, about 60 minutes.** Any time after week 10 (you need dictionaries).

## Tonight's idea

When you play Minecraft on a server, your game is the **client**: it **asks** for things ("what blocks are around me?", "I broke this block"). The server **answers** and keeps the world running for everyone.

Tonight your Python program is the client. It asks a server on the internet a question and gets an answer back.

```
your program  --- "is mc.hypixel.net online?" --->  mcsrvstat.us  --- pings --->  the Minecraft server
your program  <--- answer (a dictionary!) --------  mcsrvstat.us  <--- reply ----  the Minecraft server
```

Notice: `mcsrvstat.us` is a server to your program, **and** a client to the Minecraft server. Most of the internet is chains like this.

## Steps

### 1. Predict (5 min)
Open `server_status.py`. Which line actually talks to the internet? What do you think `data` looks like?

### 2. Run (5 min)
Run it. Hypixel is a huge public server. How many people are on it right now?

### 3. Investigate (20 min)
1. Add `print(data)` after the `data = ...` line. It's a big **dictionary**: the server's answer. Find `"players"` in it.
2. Get other things out of it: try `data["version"]` and `data["motd"]["clean"]` (the server's message of the day).
3. Paste the URL from the code (`https://api.mcsrvstat.us/3/mc.hypixel.net`) into a web browser. Same answer! Your browser is a client too.
4. Change `server` to a made-up address. What comes back?

### 4. Your server (20 min)
Put in the address of the server you two play on.
- Does it work? A server only your home network can see (a LAN world) or a Realm can't be reached by mcsrvstat.us, so it may say offline. Talk about why: the server on the internet can't see into your house.

## New words

| Word | Meaning |
|---|---|
| **client** | The program that asks. |
| **server** | The program that answers, usually on another computer. |
| **request** | The question a client sends. |
| **response** | The server's answer. |
| **API** | A server made for programs to talk to, not people. |
| **JSON** | The text format the answer comes in. Python turns it into dictionaries and lists. |

---

## Mentor notes
- This needs internet. If the network blocks it, show the URL in a browser instead.
- Good question to finish on: "when you join our Minecraft world, what is the client and what is the server?"
