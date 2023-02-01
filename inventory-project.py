import csv

class Item:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
        
class InventoryManagementSystem:
    def __init__(self):
        self.inventory = []
        
    def add_item(self, item):
        self.inventory.append(item)
        
    def remove_item(self, item_name):
        for item in self.inventory:
            if item.name == item_name:
                self.inventory.remove(item)
                break
                
    def update_item(self, item_name, field, new_value):
        for item in self.inventory:
            if item.name == item_name:
                if field == 'quantity':
                    item.quantity = new_value
                elif field == 'price':
                    item.price = new_value
                break
                
    def display_inventory(self):
        print('Inventory:')
        for item in self.inventory:
            print(f"Name: {item.name} | Quantity: {item.quantity} | Price: {item.price}")
            
    def save_inventory(self, file_name):
        with open(file_name, 'w', newline='') as csvfile:
            fieldnames = ['name', 'quantity', 'price']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for item in self.inventory:
                writer.writerow({'name': item.name, 'quantity': item.quantity, 'price': item.price})
                
    def load_inventory(self, file_name):
        with open(file_name, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                item = Item(row['name'], int(row['quantity']), float(row['price']))
                self.inventory.append(item)
                
inventory = InventoryManagementSystem()
item1 = Item('item1', 10, 5.0)
item2 = Item('item2', 20, 10.0)
inventory.add_item(item1)
inventory.add_item(item2)
inventory.display_inventory()
inventory.remove_item('item1')
inventory.display_inventory()
inventory.update_item('item2', 'quantity', 25)
inventory.display_inventory()
inventory.save_inventory('inventory.csv')
inventory.load_inventory('inventory.csv')
inventory.display_inventory()


"""
The above code creates a class Item with three attributes name, quantity, and price. It also creates a class InventoryManagementSystem with five methods add_item, remove_item, update_item, display_inventory, and save_inventory.

The add_item method allows the user to add a new item to the inventory by appending it to the inventory list. The remove_item method allows the user to remove an item from the inventory by looping through the inventory list and removing the item with the matching name. The update_item method allows the user to update the quantity or price of an item by looping through the inventory list and updating the matching item. The display_inventory method displays the current inventory by looping through the inventory list and printing the name, quantity, and price of each item.

The save_inventory method saves the inventory to a CSV file. It opens the file in write mode, creates a csv.DictWriter object, and writes the header and the rows of the inventory to the file. The load_inventory method loads the inventory from a CSV file. It opens the file in read mode, creates a csv.DictReader object, and loops through the rows of the file to create Item objects and add them to the inventory list.

Finally, the code creates an instance of the InventoryManagementSystem class, adds two items to the inventory, displays the inventory, removes one item, updates another item, saves the inventory to a file, and loads the inventory from the file.

"""