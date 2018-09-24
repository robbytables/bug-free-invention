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

class Penguin(Animal):
  def __init__(self):
    super().__init__()
    print("I am a penguin!")
    self.energy = 100

  def move(self):
    self.energy -= 5
    print("I am sliding!")

class Eagle(Animal):
  def __init__(self):
    super().__init__()
    print("I am an eagle!")
    self.energy = 20

  def move(self):
    if self.energy < 0:
      print("I'm too tired to fly...")
    else:
      print("I am flying to the sea!")

    self.energy -= 20

  def say_hi(self):
    print("Shrieeeeek!")



# If you want to test the example, uncomment the code below

# animal = Animal()
# animal.get_status()
# animal.eat(60)
# animal.get_status()
# animal.move()
# animal.get_status()
# animal.say_hi()
# print()

# penguin = Penguin()
# penguin.eat(5)
# penguin.get_status()
# penguin.move()
# penguin.get_status()
# penguin.say_hi()
# print()

# eagle = Eagle()
# eagle.say_hi()
# eagle.get_status()
# eagle.move()
# eagle.get_status()
# eagle.move()
# eagle.get_status()
# eagle.move()
# print()
