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
		
	
	def __eq__(self, other):
		
		return self.numFloors == other.numFloors
		
	def __lt__(self, other):
		
		return self.numFloors < other.numFloors
		
	def __le__(self, other):
		
		return self.numFloors <= other.numFloors
		
	def __gt__(self, other):
		
		return self.numFloors > other.numFloors
		
	def __ge__(self, other):
		
		return self.numFloors >= other.numFloors
		
	def __ne__(self, other):
		
		return self.numFloors != other.numFloors
		
	
	def __add__(self, value):
		
		self.numFloors += value
		return self.numFloors



h1 = House('ЖК "Белые Черёмушки"', 42)
h2 = House('МК "Васильевская Слобода"', 6)

h1.go_to(int(input("Введите номер этажа: ")))
h2.go_to(int(input("Введите номер этажа: ")))

# На этом моменте закончился module_5_1

print(h1)
print(h2)

print(len(h1))
print(len(h2))

print( "_" * 50, "\n")

# А на этом module_5_2

print(h1 == h2)
print(h1 < h2)
print(h1 <= h2)
print(h1 > h2)
print(h1 >= h2)
print(h1 != h2)

print("_" * 50, "\n")

h1 = h1 + 10
print(h1)

h1 += 10
print(h1)

# Не понял,зачем добавлять __radd__ и __iadd__,
# если они делают то же самое, что и функция выше.
# если это критически важно, прошу дать мне пояснение
# в ответе на задание. Зарание спасибо
#
# С уаажением, Владик.

