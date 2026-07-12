server_ip = ("10.1.1.1", "10.1.6.1", "10.4.1.1", "10.9.1.1")
print(type(server_ip))

hi=("Sarthak",)
print(type(hi)) #tuple

hi=("Nigam")
print(type(hi)) #string

server_ip(2)=44 #not mutable 
print(server_ip)

print(server_ip.index("10.1.1.1"))