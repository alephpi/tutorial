from typing import TypedDict


class Person(TypedDict):
    name: str
    age: int

person = Person(name="Alice", age=25)
person2 = Person({'name':"Bob", 'age':30})
person3 = Person({'mame':"Bob", 'age':30})
print(person)
print(person2)