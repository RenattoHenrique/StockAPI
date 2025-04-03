from repositories.BaseRepository import BaseRepository  

class ProductRepository(BaseRepository):  
    
    def __init__(self):  
        super().__init__()  

    def getAll(self):  
        query = "SELECT id, name, supplier, cost, price FROM products"  
        products = self.executeQuery(query)
        
        # Convertendo lista de tuplas para lista de dicionários
        product_list = [
            {"id": p[0], "name": p[1], "supplier": p[2], "cost": p[3], "price": p[4]}
            for p in products
        ]
        
        return product_list

    def create(self, productData):  
        query = f"INSERT INTO products (name, supplier, cost, price) VALUES ('{productData['name']}', '{productData['supplier']}', {productData['cost']}, {productData['price']})"  
        self.execute(query)  

    def details(self, id: int):  
        query = f"SELECT * FROM products WHERE products.id = {id}"  
        product = self.executeQuery(query)  
        return product  

    def update(self, id: int, productData):  
        query = f"UPDATE products SET name = '{productData['name']}', supplier = '{productData['supplier']}', cost = {productData['cost']}, price = {productData['price']} WHERE id = {id}"  
        self.execute(query)  

    def delete(self, id: int):  
        query = f"DELETE FROM products WHERE id = {id}"  
        self.execute(query)  