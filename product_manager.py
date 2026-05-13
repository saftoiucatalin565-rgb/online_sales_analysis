from product import Product

class ProductManager:
    def __init__(self):
        """Constructor pentru initializarea managerului de produse"""
        self.products = []
    
    def add_product(self, product):
        """Adauga un produs in lista"""
        self.products.append(product)
        print(f"Produs adaugat: {product.name}")
    
    def show_all_products(self):
        """Afiseaza toate produsele"""
        print("\n=== Lista Produse ===")
        if not self.products:
            print("Nu exista produse!")
        else:
            for product in self.products:
                product.display()
                print()
    
    def compute_total_inventory_value(self):
        """Calculeaza valoarea totala a inventarului"""
        total = sum(product.price * product.quantity for product in self.products)
        return total
