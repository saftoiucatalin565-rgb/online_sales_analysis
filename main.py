from product import Product
from product_manager import ProductManager

def main():
    print("=== SISTEM GESTIONARE PRODUSE - VERSIUNE MAIN ===\n")
    
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

if __name__ == "__main__":
    main()
