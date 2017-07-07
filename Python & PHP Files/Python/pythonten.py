#pythonten.py
# This script demonstrate object creation in OOP

class Inventory(object):
	totalInventory = 0
	def __init__(self, name = "Unknown", price = 0.0, quantity = 0):
		self.name_str = name
		self.price_flt = price
		self.quantity_int = quantity
		self.total = 0
		
	def value_stock(self):
		self.total = self.quantity * self.price
		return self.total
		
	def __str__(self):
		#Return string with the name and total
		return 'Name: {}. Total: {}'.format(self.name, self.total)
	
flash_drive_8gb = Inventory("USB Flash Drive", 12.99, 40)
flash_drive_8gb.value_stock() #can get same results using... Inventory.value_stock(flash_drive_8gb)
print(flash_drive_8gb.__dict__)

