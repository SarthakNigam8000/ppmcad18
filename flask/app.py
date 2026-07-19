from flask import Flask , request
app = Flask(__name__)
usersList = [

    {

        "id": 1,

        "username": "prashant",

        "name": "Prashant Dey",

        "age": 30

    },

    {

        "id": 2,

        "username": "ashish",

        "name": "Ashish Kumar",

        "age": 70

    },

    {

        "id": 3,

        "username": "sarthak",

        "name": "Sarthak Nigam",

        "age": 29

    }

]


@app.route('/', methods=["GET"])
def main():
    return "Hello World"

@app.route('/about', methods=["GET"])
def about():
    return "Hello Sarthak Nigam"

@app.route('/info', methods=["GET", "POST"])
def info():
    return "Info"

@app.route('/user/<string:username>')
def users(username):
     for i in usersList:
         if i["username"] == username:
             return f"User: {i['username']}, Age: {i['age']}, Name: {i['name']}"
         else: 
             return "No User present"
@app.route("/login", methods=["POST"])

def login():

    username = request.get_json("username")

    password = request.get_json("password")

    print(username, password)

    return username         


@app.route("/people")

def people():

    user = request.args.get("user")

    age = request.args.get("age")

    return f"user: {user} | age: {age}"         

if __name__=="__main__":
    app.run(debug=True)

