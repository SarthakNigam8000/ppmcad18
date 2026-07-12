server_list1 = ["hello", "hi", "22", "TRUE",55,44,33,99,00]
server_list2 = ["Nigam", "hi", "33", "FALSE"]

#print(server_list1)
#print(server_list2)

server_list1.append("Sarthak")
#print(server_list1)

server_list2.append("Sarthak")
#print(server_list2)


server_list1.extend(server_list2)
#print(server_list1)


sample_list = [56,77,[34,55]]
#print(sample_list[2])
#print(sample_list[2][1])

sample_list.insert(1,"Sarthak")
sample_list.clear()
#print(sample_list)

#print(server_list1[0:7:3])

#if "Sarthak" in server_list1:
    #print("He is here")
#else:
    #print("He is not her ")    


#print(server_list1.count("Sarthak"))
#print(server_list1)

server_list3 = ["hello", "hi", "22", "TRUE"]
#server_list3.sort(reverse=True)
#print(server_list3)
#print(len(server_list3))

for i in server_list3:
    print(i)


for i,j in enumerate(server_list3):
    print(i,j)