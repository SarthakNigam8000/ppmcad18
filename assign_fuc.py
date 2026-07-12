users = [

    {

        "username": "prashant",

        "password": "pass123"

    },

    {

        "username": "mohan",

        "password": "pass1235"

    },

    {

        "username": "rishav",

        "password": "rishav123"

    },

]
 
name =input("Enter the name ")
password = input("Enter the password ")

def usr(name,password):
    for i in users.values():
        if i[0] == name and i[1] == password:
            print("Details are present")
        else:
            print("Details are not present")    


(usr(name,password))
