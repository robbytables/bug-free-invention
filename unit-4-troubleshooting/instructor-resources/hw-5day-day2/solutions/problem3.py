class Animal:
  def __init__(self):
    print("I'm coming to life!")
    self.energy = 50

  def eat(self, amount):
    self.energy += amount

  def move(self):
    self.energy -= 10
    print("I am running!")

  def say_hi(self):
    print("Meep!")

  def get_status(self):
    print("My energy level is", self.energy)

    if self.energy < 0:
      print("I'm starving!")
    elif self.energy < 50:
      print("I'm getting hungry!")
    elif self.energy <= 100:
      print("I'm happily full.")
    else:
      print("I'm feeling stuffed!")


# If you want to test the example code, uncomment the below code

# print("Making my first animal")
# first_animal = Animal()
# first_animal.get_status()
# first_animal.eat(55)
# first_animal.get_status()
# first_animal.move()
# first_animal.get_status()
# print("first animal saying hi")
# first_animal.say_hi()
# print()

# print("Making a second animal now")
# second_animal = Animal()
# second_animal.get_status()
# second_animal.eat(-45)
# second_animal.get_status()
# second_animal.move()
# second_animal.get_status()
# print("second animal saying hi")
# second_animal.say_hi()
