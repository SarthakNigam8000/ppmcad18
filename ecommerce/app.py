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
    # Frontend ya UI se jo JSON data aa raha hai, usko extract kar rahe hain
    data = request.get_json() 
                            
    name = data.get("name")
    qty = data.get("quantity")
    price = data.get("price")
    sku_id = data.get("sku_id")
    category = data.get("category")

    # Inputs ko ek dictionary mein daal rahe hain taaki MongoDB mein save kar sakein
    product = {
        "name": name,
        "quantity": qty,
        "price": price,
        "sku_id": sku_id,
        "category": category
    }

    # Product document ko MongoDB collection ke andar insert kar rahe hain
    result = products_collection.insert_one(product) 
    return {"msg": "data added"}


@app.route("/search")
def searchproduct():
    # URL se 'name' query parameter ki value nikal rahe hain (jaise: /search?name=apple)
    name = request.args.get("name") 

    # Database mein product ko dhoondh rahe hain; ye ek object/dictionary return karta hai
    product = products_collection.find_one({"name": name}) 
    
    # MongoDB ke '_id' (ObjectId) ko string mein convert kar rahe hain taaki JSON mein error na aaye
    product["_id"] = str(product["_id"]) 

    return {"msg": product} 
 

if __name__ == "__main__":
    app.run(debug=True, port=3005)