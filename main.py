from product import Product
from product_manager import ProductManager

def main():
    print("=== SISTEM GESTIONARE PRODUSE ===\n")
    
    # Cream ProductManager
    manager = ProductManager()
    
    # Adaugam produse
    product1 = Product("Laptop Dell", 3500, 10)
    product2 = Product("Mouse Logitech", 150, 25)
    product3 = Product("Tastatura Mecanica", 400, 15)
    product4 = Product("Monitor LG", 1200, 8)
    product5 = Product("Webcam HD", 250, 20)
    
    manager.add_product(product1)
    manager.add_product(product2)
    manager.add_product(product3)
    manager.add_product(product4)
    manager.add_product(product5)
    
    # Afisam toate produsele
    manager.show_all_products()
    
    # Calculam valoarea totala
    total_value = manager.compute_total_inventory_value()
    print(f"=== Valoare totala inventar: {total_value} lei ===\n")

if __name__ == "__main__":
    main()
