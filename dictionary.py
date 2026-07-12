server = {
    "name": "Server-1",
    "ip" : "10.1.11.1",
    "cpu": 4,
    "Memory": 8
}

print(server.get("name"))

server["name"] = "Sarthak"

print(server.get("name"))

for i in server.values():
    print(i)


