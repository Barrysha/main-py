class house():
	
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



h1 = house('ЖК "Белые Черёмушки"', 42)
h2 = house('МК "Васильевская Слобода"', 6)

h1.go_to(int(input("Введите номер этажа: ")))
h2.go_to(int(input("Введите номер этажа: ")))