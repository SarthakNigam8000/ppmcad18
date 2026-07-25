# Flask aur request module import kar rahe hain
from flask import Flask, request

# Flask application create kar rahe hain
app = Flask(__name__)

# Empty list jisme users ka data store hoga
usersList = []


# Home Route
# URL: http://127.0.0.1:5000/
# Sirf GET request allow hogi
@app.route('/', methods=["GET"])
def main():
    return "Hello World"


# About Route
# URL: http://127.0.0.1:5000/about
@app.route('/about', methods=["GET"])
def about():
    return "Hello Sarthak Nigam"


# Info Route
# GET aur POST dono requests accept karega
@app.route('/info', methods=["GET", "POST"])
def info():
    return "Info"


# Dynamic Route
# URL me username pass karna hoga
# Example:
# http://127.0.0.1:5000/user/sarthak
@app.route('/user/<string:username>')
def users(username):

    # usersList me loop chala kar username search kar rahe hain
    for i in usersList:

        # Agar username match ho gaya
        if i["username"] == username:

            # User ki details return kar do
            return f"User: {i['username']}, Age: {i['age']}, Name: {i['name']}"

    # Agar username nahi mila
    return "No User present"


# Login API
# Sirf POST request allow hai
@app.route("/login", methods=["POST"])
def login():

    # Client se bheja gaya JSON data receive kar rahe hain
    data = request.get_json()

    # JSON me se username aur password nikal rahe hain
    username = data.get("username")
    password = data.get("password")

    # Console me print hoga
    print(username, password)

    # Response me username return kar rahe hain
    return username


# Query Parameters Example
# Example:
# http://127.0.0.1:5000/people?user=Sarthak&age=24
@app.route("/people")
def people():

    # URL ke query parameters read kar rahe hain
    user = request.args.get("user")
    age = request.args.get("age")

    # Response return kar rahe hain
    return f"user: {user} | age: {age}"


# Yeh ensure karta hai ki app directly run ho tabhi server start ho
if __name__ == "__main__":

    # Debug=True se code change hote hi server automatically restart ho jata hai
    # Aur errors browser me clearly dikhte hain
    app.run(debug=True)