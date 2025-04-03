from workers.ProductWorker import ProductWorker  
from flask import request, jsonify  

class ProductController():  
    def __init__(self):  
        self.productWorker = ProductWorker()  

    def getAll(self):  
        try:   
            products = self.productWorker.getAll()  
        except:   
            return jsonify({"error": "Falha ao tentar recuperar produtos"}), 204  

        if len(products) == 0:  
            return jsonify({"message": "nenhum produto cadastrado"}), 204  

        return jsonify({"products": products}), 200

    def create(self):  
        data = request.get_json()  
        if not data: return jsonify({"error": "Nenhum dado informado"}), 400  
        if not data["name"]: return jsonify({"error": "Nome do produto não informado"}), 400  
        if not data["supplier"]: return jsonify({"error": "Nome do fornecedor não informado"}), 400  
        if not data["cost"]: return jsonify({"error": "Custo do produto não informado"}), 400  
        if not data["price"]: return jsonify({"error": "Preço do produto não informado"}), 400  

        product = {}  
        try:  
            name = data["name"].strip()  
            supplier = data["supplier"].strip()  
            cost = float(data["cost"].strip())  
            price = float(data["price"].strip())  

            product["name"] = name  
            product["supplier"] = supplier  
            product["cost"] = cost  
            product["price"] = price  
        except:  
            return jsonify({"error": "Dados inválidos"}), 400  

        self.productWorker.create(product)  

        return jsonify({"message": "Produto Criado com sucesso"}), 201  
    
    def details(self, id: int):  
        if(id <= 0):   
            return jsonify({"error": "id inválido"}), 400  
        try:  
            product = self.productWorker.details(id)  
        except:  
            return jsonify({"error": "Falha ao deletar produto"}), 500  
        if not product:  
            return jsonify({"error": "Produto não encontrado"}), 404  
        return jsonify({"product": product}), 200  

    def update(self, id: int):  
        data = request.get_json()  
        if not data:   
            return jsonify({"error": "Nenhum dado informado"}), 400  
        if not data["name"]: return jsonify({"error": "Nome do produto não informado"}), 400  
        if not data["supplier"]: return jsonify({"error": "Nome do fornecedor não informado"}), 400  
        if not data["cost"]: return jsonify({"error": "Custo do produto não informado"}), 400  
        if not data["price"]: return jsonify({"error": "Preço do produto não informado"}), 400  

        product = {}  
        try:  
            name = data["name"].strip()  
            supplier = data["supplier"].strip()  
            cost = float(data["cost"].strip())  
            price = float(data["price"].strip())  
            product["name"] = name  
            product["supplier"] = supplier  
            product["cost"] = cost  
            product["price"] = price  
        except:  
            return jsonify({"error": "Dados inválidos"}), 400  
        
        try:   
            self.productWorker.update(id, product)  
        except:   
            return jsonify({"error": "Falha ao tentar atualizar produto"}), 500  
        
        return jsonify({"message": "produto atualizado com sucesso"}), 200  