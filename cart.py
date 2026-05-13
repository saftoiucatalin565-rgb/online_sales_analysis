class Cart:
    def __init__(self):
        """Constructor pentru initializarea cosului"""
        self.cart_items = []
    
    def add_item(self, product, quantity=1):
        """Adauga produs in cos"""
        self.cart_items.append({
            'product': product,
            'quantity': quantity
        })
        print(f"Adaugat in cos: {product.name} x {quantity}")
    
    def calculate_total(self):
        """Calculeaza totalul cosului"""
        total = sum(item['product'].price * item['quantity'] for item in self.cart_items)
        return total
    
    def show_cart(self):
        """Afiseaza continutul cosului"""
        print("\n=== Cosul de Cumparaturi ===")
        if not self.cart_items:
            print("Cosul este gol!")
        else:
            for item in self.cart_items:
                product = item['product']
                qty = item['quantity']
                print(f"{product.name} x {qty} = {product.price * qty} lei")
            print(f"\nTotal cos: {self.calculate_total()} lei")
