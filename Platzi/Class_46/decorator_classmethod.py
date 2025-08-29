class Person:
  species = "Homo sapiens"

  def __init__(self, name, age):
    self.name = name
    self.age = age

  @classmethod
  def alt_constructor(cls, person_name_age):
    name, age = person_name_age.split("-")
    return cls(name, int(age))
  
  @classmethod
  def get_species(cls):
    return cls.species
  

person_one = Person("NameOne", 25)
print(person_one.get_species())

#@classmethod being used as alternative constructor
person_two = Person.alt_constructor("Oscar-25")
print(person_two.name, person_two.age)

#@classmethod being used as cls
person_three = Person.get_species()
print(person_three)