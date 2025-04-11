from Dog import Dog
from Cat import Cat

dog = Dog("Buddy", "dog", 10)
cat = Cat("Whiskers", "cat")

print(f"{dog.name} makes: {dog.make_sound()}")
print(f"{cat.name} makes: {cat.make_sound()}")

