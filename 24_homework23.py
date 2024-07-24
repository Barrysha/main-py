class House():
	
	def __init__(self, name, numFloors):
		
		self.name = name
		self.numFloors = numFloors
	
			
	def go_to(self, new_floor):
		
		if new_floor < 1 or new_floor > self.numFloors:
			print("такого значения не существует")
		else:
			if type(new_floor) is int:
				for i in range(new_floor):
					print(i + 1)
				print("_"*50, "\n")
	
	
	def __len__(self):
		
		return self.numFloors
		
		
	def __str__(self):
		
		return f"Название: {self.name}, кол-во этажей: {self.numFloors}"



h1 = House('ЖК "Белые Черёмушки"', 42)
h2 = House('МК "Васильевская Слобода"', 6)

h1.go_to(int(input("Введите номер этажа: ")))
h2.go_to(int(input("Введите номер этажа: ")))

print(h1)
print(h2)

print(len(h1))
print(len(h2))