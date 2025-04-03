from flask import Flask
from flask_cors import CORS
from controllers.ProductController import ProductController

api = Flask(__name__)
CORS(api)

productController = ProductController()

@api.route("/products", methods=["GET"])
def listProducts(): return productController.getAll()

@api.route("/products/details/<int:id>", methods=["GET"])
def productDetails(id:int): return productController.details(id)

@api.route("/products/create", methods=["POST"])
def createProduct(): return productController.create()

@api.route("/products/update/<int:id>", methods=["PUT"])
def updateProduct(id:int): return productController.update(id)

@api.route("/products/delete/<int:id>", methods=["DELETE"])
def deleteProduct(id:int): return productController.delete(id)

# api.run(host="0.0.0.0", port=5000, debug=True)