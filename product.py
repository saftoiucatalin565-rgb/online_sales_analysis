class Product:
    def __init__(self, name, price, quantity):
        """Constructor pentru initializarea produsului"""
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def display(self):
        """Afiseaza informatii despre produs"""
        print(f"Produs: {self.name}")
        print(f"  Pret: {self.price} lei")
        print(f"  Cantitate: {self.quantity}")
    
    def update_quantity(self, new_quantity):
        """Actualizeaza cantitatea produsului"""
        self.quantity = new_quantity
        print(f"Cantitatea pentru {self.name} a fost actualizata la {self.quantity}")
