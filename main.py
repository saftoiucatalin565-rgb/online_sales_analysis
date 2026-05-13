from product import Product
from product_manager import ProductManager
from cart import Cart
import random

def main():
    print("=== SISTEM GESTIONARE PRODUSE SI COS ===\n")
    
    # Cream ProductManager
    manager = ProductManager()
    
    # Adaugam produse
    product1 = Product("Laptop Dell", 3500, 10)
    product2 = Product("Mouse Logitech", 150, 25)
    product3 = Product("Tastatura Mecanica", 400, 15)
    
    manager.add_product(product1)
    manager.add_product(product2)
    manager.add_product(product3)
    
    # Test eliminare produs
    print("\n=== Test Eliminare Produs ===")
    manager.remove_product("Mouse Logitech")
    manager.show_all_products()
    
    # Cream cos si adaugam produse
    cart = Cart()
    cart.add_item(product1, 2)
    cart.add_item(product3, 1)
    
    # Afisam cosul
    cart.show_cart()

if __name__ == "__main__":
    main()
