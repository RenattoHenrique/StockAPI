from repositories.ProductRepository import ProductRepository

class ProductWorker():
    def __init__(self):
        self.productRepository = ProductRepository()
        
    def getAll(self): return self.productRepository.getAll()
    
    def create(self, product): self.productRepository.create(product)
    
    def details(self, id:int): return self.productRepository.details(id)
    
    def update(self, id:int, product): self.productRepository.update(id,product)

    def delete(self, id:int): self.productRepository.delete(id)