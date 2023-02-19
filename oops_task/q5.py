# q5.What is method overriding in python?
# Ans: Method overriding is a feature of object-oriented programming languages where the subclass or child class can provide the program with specific characteristics
# 	or a specific implementation process of data provided that are already defined in the parent class or superclass.

# Eg:
class Parent():

	def __init__(self):
		self.value = "Inside Parent"

	def show(self):
		print(self.value)

class Child(Parent):

	def __init__(self):
		self.value = "Inside Child"

	def show(self):
		print(self.value)

obj1 = Parent()
obj2 = Child()

obj1.show()
obj2.show()
