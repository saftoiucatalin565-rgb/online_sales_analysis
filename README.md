# Online Sales Analysis

## Descriere
Proiect Python pentru gestionarea produselor si a cosului de cumparaturi folosind programare orientata pe obiecte (OOP).

## Clase Implementate

### Product
- `__init__(name, price, quantity)` - Constructor
- `display()` - Afiseaza informatii despre produs
- `update_quantity(new_quantity)` - Actualizeaza cantitatea

### ProductManager
- `__init__()` - Initializeaza lista de produse
- `add_product(product)` - Adauga produs
- `show_all_products()` - Afiseaza toate produsele
- `compute_total_inventory_value()` - Calculeaza valoarea totala
- `remove_product(product_name)` - Elimina produs dupa nume

### Cart
- `__init__()` - Initializeaza cosul
- `add_item(product, quantity)` - Adauga produs in cos
- `calculate_total()` - Calculeaza totalul cosului
- `show_cart()` - Afiseaza continutul cosului

## Utilizare

```bash
python3 main.py
