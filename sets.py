server_ip = {"1.1.0.1.1.", "10.1.6.1", "10.4.1.1", "10.9.1.1"}

#server_ip.add("77788")
#server_ip.update(("10.1.1.1","10.1.1.9")). # it just adds new value bcz it is not ordered
#no duplicate

server_ip.remove(("10.9.1.1")) # it works
server_ip.add("Sarthak")
print(server_ip)