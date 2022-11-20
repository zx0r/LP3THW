class Parent(object):
	def implicit(self):
		print("PARENT implicit()")

	def override(self):
		print("PARENT override()")

	def altered(self):
		print("PARENT altered()")

class Child(Parent):
	def __init__(self, stuff):
		self.stuff = stuff
		super(Child, self).__init__()

	def override(self):
		print("CHILD override()")

	def altered(self):
		print("CHILD, before PARENT altered()")
		super(Child, self).altered()
		print("CHILD, after PARENT altered()")

class Other(object):
	def override(self):
		print("OTHER override()")

	def implicit(self):
		print("OTHER implicit()")

	def altered(self):
		print("OTHER altered()")

class OtherChild(object):
	def __init__(self):
		self.other = Other()

	def implicit(self):
		self.other.implicit()

	def override(self):
		print("OTHER CHILD override()")

	def altered(self):
		print("OTHER CHILD, before OTHER altered()")
		self.other.altered()
		print("OTHER CHILD, after OTHER altered()")

print("*** Inheritance: ***")
dad = Parent()
son = Child("some stuff to not break on init")
otherson = OtherChild()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()
print("\n*** Composition: ***")
otherson.implicit()
otherson.override()
otherson.altered()
