from Dog import Dog
from Cat import Cat

dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Black")

# Display the attributes and methods
print(f"{dog.name} is a {dog.breed} and makes: {dog.make_sound()}")
print(f"{cat.name} is a {cat.color} cat and makes: {cat.make_sound()}")