from flask import Flask, request

from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("/")

database = client["b18a"]

users_collection = database["New"]

 

@app.route('/', methods=["GET"])

def main():

    return "Hello to ecommerce!"


 

# @app.route("/people")

# def people():

#     user = request.args.get("username")

#     age = request.args.get("age")

#     result = users_collection.insert_one({"username": user, "age": age}) # to insert the data in the DB

#     return f"user: {user} | age: {age}"

 

if __name__=="__main__":

    app.run(debug=True, port=3005)