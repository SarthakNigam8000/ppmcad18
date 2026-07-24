from flask import Flask, request
from pymongo import MongoClient
from flask_cors import CORS

app = Flask(__name__)

client = MongoClient("")
database = client["b18a"]
products_collection = database["products"]

CORS(app)

@app.route('/', methods=["GET"]) 
def main(): 
    return "Hello to ecommerce!"


@app.route('/addproduct', methods=["POST"])
def addproduct():
    data = request.get_json() # this is the object or u can say it like dic
                            # here we are getting the inputs from the UI 
    name = data.get("name")
    qty = data.get("quantity")
    price = data.get("price")
    sku_id = data.get("sku_id")
    category = data.get("category")

                                        # converting the inputs to dic 
    product = {
        "name": name,
        "quantity": qty,
        "price": price,
        "sku_id": sku_id,
        "category": category
    }

    result = products_collection.insert_one(product) # inserting the list.
    return {"msg": "data added"}


@app.route("/search")
def searchproduct():
    name = request.args.get("name") #takes the value from the URL

    product = products_collection.find_one({"name": name}) #finds the collection naming: name, its returns object and we cannot print directly
    product["_id"] = str(product["_id"]) #it will covert the obj to str 

    return {"msg": product} # now here we can now print after the conversion
 

if __name__=="__main__":

    app.run(debug=True, port=3005)