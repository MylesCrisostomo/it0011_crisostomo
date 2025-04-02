class Product:
    def __init__(self, pid, name, desc, price):
        self.pid = pid
        self.name = name
        self.desc = desc
        self.price = price
    
    def display(self):
        print(f"{self.pid:5} | {self.name:20} | {self.desc:30} | ₱{self.price:.2f}")

class StoreSystem:
    def __init__(self):
        self.inventory = {}
    
    def add_product(self):
        try:
            pid = int(input("Enter product ID: "))
            if pid in self.inventory:
                print("ID already exists!")
                return
            
            name = input("Enter product name: ").strip()
            desc = input("Enter description: ").strip()
            price = float(input("Enter price: "))
            
            if price < 0:
                print("Price can't be negative!")
                return
                
            self.inventory[pid] = Product(pid, name, desc, price)
            print(f"{name} added successfully!")
            
        except ValueError:
            print("Invalid input! Please enter numbers for ID and price.")

    def show_products(self):
        if not self.inventory:
            print("\nNo products in inventory!\n")
            return
            
        print("\n" + "="*75)
        print("ID    | Name                | Description               | Price")
        print("="*75)
        for product in self.inventory.values():
            product.display()
        print("="*75 + "\n")

    def modify_product(self):
        try:
            pid = int(input("Enter product ID to update: "))
            if pid not in self.inventory:
                print("Product not found!")
                return
                
            print("\nLeave blank to keep current value:")
            current = self.inventory[pid]
            
            name = input(f"New name [{current.name}]: ") or current.name
            desc = input(f"New description [{current.desc}]: ") or current.desc
            
            price_input = input(f"New price [{current.price}]: ")
            price = float(price_input) if price_input else current.price
            
            if price < 0:
                print("Price can't be negative!")
                return
                
            self.inventory[pid] = Product(pid, name, desc, price)
            print("Product updated!")
            
        except ValueError:
            print("Invalid price! Update cancelled.")

    def remove_product(self):
        try:
            pid = int(input("Enter product ID to remove: "))
            if pid not in self.inventory:
                print("Product not found!")
                return
                
            product = self.inventory.pop(pid)
            print(f"{product.name} removed from inventory!")
            
        except ValueError:
            print("Invalid ID! Please enter a number.")

def show_menu():
    print("\n" + "="*30)
    print("  STORE INVENTORY SYSTEM")
    print("="*30)
    print("[1] Add Product")
    print("[2] View Products")
    print("[3] Update Product")
    print("[4] Remove Product")
    print("[5] Exit")
    print("="*30)

def run_system():
    store = StoreSystem()
    
    while True:
        show_menu()
        choice = input("Enter choice (1-5): ")
        
        if choice == "1":
            store.add_product()
        elif choice == "2":
            store.show_products()
        elif choice == "3":
            store.modify_product()
        elif choice == "4":
            store.remove_product()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    run_system()