breakfast = ["Fruit Loops", "Wheaties", "Captain Crunch"]

def cereal_time():
  for cereal in breakfast:
    last_letter = cereal[-1]
    if last_letter == "s":
      print(cereal, "are yummy!")
    else:
      print(cereal, "is yummy!")

cereal_time()
