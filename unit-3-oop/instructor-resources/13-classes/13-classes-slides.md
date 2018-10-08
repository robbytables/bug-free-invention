## ![](http://nagale.com/ga-python/images/GA_Cog_Medium_White_RGB.png)  {.separator}

<h1>Python Programming: Objects and Classes</h1>


<!--

## Overview
This lesson walks through creating classes in Python. The lesson starts with We Dos for creating a class and instantiating objects from that class. It's followed by a We Do for class and instance variables. It ends with a few partner exercises, then a series of Knowledge Checks.

## Learning Objectives
In this lesson, students will:

- Define a class.
- Instantiate an object from a class.
- Create classes with class variables.


## Duration
50 MINUTES

## Suggested Agenda

| Time | Activity |
| --- | --- |
| 0:00 - 0:03 | Welcome |
| 0:03 - 0:10 | Class Overview |
| 0:10 - 0:25 | Creating Classes |
| 0:25 - 0:30 | Class Variables |
| 0:30 - 0:47 | Exercises |
| 0:47 - 0:50 | Summary |

## In Class: Materials
- Projector
- Internet connection
- Python 3
-->

---

## Learning Objectives

*After this lesson, you will be able to…*

- Define a class.
- Instantiate an object from a class.
- Create classes with default instance variables.

---

## Blueprints

All cars have things that make them a `Car`. Although the details might be different, every type of car has the same basics — it's off the same blueprint, with the same properties and actions.

![](https://s3.amazonaws.com/ga-instruction/assets/programming-fundamentals/class-objects-car.png)

- Property: A shape (could be hatchback or sedan).
- Property: A color (could be red, black, blue, or silver).
- Property: Seats (could be between 2 and 5).
- Action: Can drive.
- Action: Can park.

<aside class="notes">

**Talking Points:**

- When we make a car, we can vary the values of these properties. Some cars have economy engines, some have performance engines. Some have four doors, others have two. However, they are all types of `Car`s.


**Teaching Tips:**

- Point out the small "c" versus the big "C"!
- Encourage students to think of other commonalities of cars — get them thinking about an archetypal car.


</aside>

---

## Introduction: Objects and Classes

These properties and behaviors can be thought of as variables and functions.

`Car` blueprint:

- Properties (variables): `shape`, `color`, `seats`
- Actions (functions): `drive()` and `park()`

An actual car might have:

```python
# **Properties - Variables**:
- shape = "hatchback"
- color = "red", "black", "blue", or "silver"
- seats = 2

# **Actions - Functions:**
- drive()
- park()
- reverse()
```

**Discussion:** What might a blueprint for a chair look like?

<aside class="notes">

**Teaching Tips:**

- Give more examples on the board, both real-world and what students have seen.
- Get students to where they are able to define the concept of a class. Can they come up with examples, like the chair? (Feel free to change the chair to something else!)

**Talking Points:**

- Every day, we interact with objects like chairs, beverages, cars, other people, etc. These objects have properties that define them and behaviors we can execute to interact with them.

</aside>

---

## Discussion: Python Classes

In Python, the concept of blueprints and objects is common. A **class** is the blueprint for an **object**. Everything you declare in Python is an object, and it has a class.

Consider the `Dictionary` class. There are three defining features for a class:

1. Variables: The keys and values in a `Dictionary` are the variables. They aren't, however, publicly accessible without use of indexing.
1. Functions: `get()`, `items()`, `keys()`, `values()`, and more.
1. Initialization: `dict(list_of_tuples)` will return a new `Dictionary()` object, initialized with the values passed in.


What behaviors and properties do you think are in the `Set` class? The `List` class?


<aside class="notes">

**Teaching Tips:**

- This is a tough slide, so spend a few minutes to make sure students get it.
- Have a discussion! Write on the board and have students brainstorm what's common about dictionaries. This doubles as a dictionary and set review.
- If you think it will help, pull up the `List` class specification — although this might be better to do after students learn the class syntax.

**Talking Points:**

- Similarly, you will hear people say that "everything is an object" in Python. Python is an object-oriented programming language.
- What this means is that nearly every variable you declare actually has a set of properties and functions that it can use — it is an object.
- Every string, number, list, dictionary, etc. has a set of behaviors and properties that are "baked in" because they are instances of a class.
- Every list you declare has properties (the values in it) and behaviors — functions like `append()` and `pop()`.
- In Python, there is a built-in `List` class, which has the ability to hold values, and built-in list functions like `append()` and `pop()`. When you declare a list in Python, you're making your own list object that's a variation of the `List` class.
</aside>

---

## Discussion: A `Dog` Class

We can make a class for anything! Let's create a `Dog` class.

The objects might be `greyhound`, `goldenRetriever`, `corgi`, etc.

Think about the `Dog` blueprint. What variables might our class have? What functions?

![](https://s3.amazonaws.com/ga-instruction/assets/programming-fundamentals/class-dog-blueprint.png)

**Pro tip:** When functions are in a class, they are called "methods." They're the same thing!

**Pro tip:** While objects are named in snake_case, classes are conventionally named in TitleCase, while instances of classes are named in camelCase.

<aside class="notes">

**Teaching Tips:**

- Try to lead students toward name, age, color, and barking — that's what will be in the class we create.

</aside>


---


## We Do: Defining Classes

Follow along! Let's create a new file, `Dog.py`.

Class definitions are similar to function definitions, but instead of `def`, we use `class`.

Let's declare a class for `Dog`:

```python
class Dog():
 # We'll define the class here.
 # Our dog will have two variables: name and age.
```

![](https://s3.amazonaws.com/ga-instruction/assets/programming-fundamentals/class-dog-name-age.png)

**Pro tip:** Files are usually named for their class, so the `Dog` class is in `Dog.py`.

<aside class="notes">

**Teaching Tips:**

- Make sure students do this with you! Practicing syntax is key.

**Talking Points:**

- It's very common in programming to make our own classes to organize data in the ways we want. Python gives us, for example, a string and an integer.
- What if we want to store a bunch of data where each item contains a string **and** an integer **and** a function that prints them out nicely?
- We can make a class for that, and then each object we make from that class will have that all baked in.
</aside>

---

## A Brief Aside: Named Args

Refresher: Arguments are named variables passed to functions. i.e.:

```python
# Plays the given song, setting the client to play the song at the given volume
def play_song(song_title, volume):
  song = music_client.get(song_title)
  song.play(volume)
```

Arguments can be assigned *default values*, using the same syntax as variable definition.

```python
# Plays the given song, setting the client to play the song at the given volume,
# or with volume = 0 if no volume is passed in.
def play_song(song_title, volume=0):
  song = music_clinet.get(song_title)
  song.play(volume)
```

This is useful when you need to have a value, or want to allow "preferred" values to be overridden. 

---

## We Do: The `__init__` Method

What first? Every class has a `__init__` method. These methods are *always* defined before any other methods.

* Populates variables with important information.
* Should not be responsible for any object functionality.
* Short for "initialize."
  * "Every time you make an object from this class, do what's in here."

Let's add this:

```python
class Dog():

  def __init__(self, name="", age=0):
    # Note the optional parameters and defaults.
    self.name = name # All dogs have a name.
    self.age = age # All dogs have an age.
```

*Note: `self` means "each individual object made from this class." Not every "dog" has the same name!*


<aside class="notes">

**Teaching Tips:**

- `Self` is tough! It will make more sense after you start creating objects. Don't spend more than a few minutes on it — go back to it when comparing instance versus class variables.
- Call out the default values, or optional parameters, as we very recently learned them.
- Method means function!

**Talking Points:**

- When we make an object, we'll first set its variables.
- The first argument passed to the `__init__` function, `self`, is required when defining methods for classes. The `self` argument is a reference to a future instantiation of the class. In other words, `self` refers to each individual dog.
- This lets each object made from a class keep references to its own data and function members. Not every "dog" has the same attributes, so we want individual cars to maintain their own attributes.
- Python allows us to provide default values for parameters in any function we provide. Here, if no `name` or `age` values are provided when a `Dog` is initialized, they will default. To create default values, we assign values to the parameter `capacity` *inside* the parentheses. You've seen this!
</aside>
---

## We Do: Adding a `bark_hello()` Method

All dogs have the behavior `bark`, so let's add that. This is a regular function (method), just inside the class!

```python
class Dog():

  def __init__(self, name="", age=0):
  # Note the defaults.

    self.name = name # All dogs have a name.
    self.age = age # All dogs have an age.

  # All dogs have a bark function.
  def bark_hello(self):
    print("Woof! I am called", self.name, "; I am", self.age, "human-years old.")
```

We're done defining the class!

<aside class="notes">

**Teaching Tips:**

- Note that it takes `self`! This will be tough to remember. Point out that it matches how the variable was declared.
</aside>

---

## Another Brief-ish Aside: Instantiating Objects From Classes

We call our class name like we call a function — passing in arguments, which go to the `init`.

Add this under your class (non-indented!):

```python
# Declare the objects.
yuki = Dog("Yuki", 4)
snukie = Dog("Snukie", 5)
maxx = Dog("Maxx", 8)

# Test them out!
yuki.bark_hello()
print("This dog's name is", yuki.name)
print("This dog's age is", yuki.age)
snukie.bark_hello()
maxx.bark_hello()
```

Try it! Run `Dog.py` like a normal Python file: `python Dog.py`.

<aside class="notes">

**Teaching Tips:**

- Map out that these variables go to `__init__` to get created. All arguments go to `__init__`!
- They have a working class! Go back through the whole code and make sure students understand.
- After running this, stop and check for understanding.

**Talking Points:**

- This will create a new object according to our `Dog` class specification.
- Python runs our `__init__` method to initialize the object.
- Here, we are telling our `__init__` method to set the name of this `dog` to `'Gracie'` and set her age to `8` years old.
- Even though `self` is listed as a parameter for the `bark_hello()` function, we don't pass it into the function. It happens automatically.
</aside>

---


## Quick Review: Classes

A class is a blueprint for an object. Some classes are built into Python, like `List`. We can always make a `list` object.

We can make a class for anything!

```python
# Created like a function; TitleCase
class Dog():

  # __init__: A method (function) that happens just once, when the object is created.
  def __init__(self, name="", age=0): # What's passed in to the class is used here.
    # Set variables for each.
    self.name = name
    self.age = age
    print(name, "created.") # This will run when the __init__ method is called.

  # Classes can have as many methods (functions) as you'd like.
  def bark_hello(self):
    print("Woof! I am called", self.name, "; I am", self.age, "human-years old.")

fox = Dog("Fox") # Creating the object calls __init__. Objects are snake_case.
print("This dog's name is", fox.name) # The object now has those variables!
fox.bark_hello() # The object now has those methods and variables!
```

<aside class="notes">

**Teaching Tips:**

- Add your own reasons for why classes are useful.
- Do a quick check for understanding.
- Run down the comments in the code like they're bullet points!

</aside>
---

## Discussion: What About Wahtah?

Let's make a `WaterGlass` class.

* What variables would a glass of water have?
* What methods?

<aside class="notes">

**Teaching Tips:**

- Have the students discuss suggestions for properties for a `WaterGlass` class.
- The exercise has `capacity`, `amount`, `fill`, `empty`, and `drink`.

</aside>

---

## A Potential `WaterGlass` Class

We could say:

Variables:

* A total `capacity`.
* A current `amount`.

Methods:

* `fill()` our glass.
* `empty()` our glass.
* `drink()` some water from our glass.

<aside class="notes">

**Talking Points:**

- Given a well-defined glass of water, we can use the class definition to create **instances** of the class.
- Each **instance** of the `WaterGlass` class can have a different `capacity` and keep track of different `amounts`.
- Although different, properties are affected by actions like `fill()`, `empty()`, and `drink()` similarly.
</aside>

---

## Example: A `WaterGlass` Class


Here's what a `WaterGlass` class definition might look like in Python:

```python
class WaterGlass():
  def __init__(self, capacity):
    # Python executes when a new glass of water is created.
    self.capacity = capacity # Total ounces the glass holds.
    self.amount = 0 # Current ounces in the cup. All glassess start empty!

  def fill(self):
    self.amount = self.capacity

  def empty(self):
    self.amount = 0

  def drink(self, amount_drank):
    self.amount -= amount_drank
    # If it's empty, it stays empty!
    if (self.amount <= 0):
      self.amount = 0

steves_cup = WaterGlass(12)  # Gotta stay hydrated.
yis_cup = WaterGlass(26)    # HYDRATION IS LIFE
brandis_cup = WaterGlass(2)  # Just a quick sip.
```

<aside class="notes">

**Teaching Tips:**

- This is the only slide, so just a demo. Talk through each line again to remind students what it does. Copy this to a file and run it!
- This class doesn't take in `amount`! It's set as a variable, but not passed in. Call it out and explain.
- Remind students that the object declarations have to go below the class. Show the error that occurs if you try calling `steves_cup` first.
- Call each function — `fill()`, `drink()` with a different number for each, and printing the amount left with `cup.amount`.

</aside>

---

## Quick Knowledge Check:

```python
class WaterGlass():
  def __init__(self, capacity=8):
    self.capacity = capacity
    self.amount = 0
```

When will the capacity be `8`?

<aside class="notes">

**Talking Points:**

- See if students can answer this.
- Answer: When no capacity is passed in when it's declared.
- After giving the answer, demo it!

</aside>


---

## A Second Type Of Var: Class Variables

Variables can be set on the class level, applying to all objects of that class. 

Rather than referencing these variables with the `self.var` syntax, we access them with the name of the class, i.e. `Class.var`

```python
class Dog():
  number_of_dogs_adopted = 0

  def __init__(self, name):
    self.name = name
    Dog.number_of_dogs_adopted += 1

  def display_info(self):
    print(name, "has been adopted! So far,", Dog.number_of_dogs_adopted, "have been adopted!")
```

These variables should be used *very* carefully, as any object of this type has access to them.

They also can be accessed publicly- let's see this in a REPL.


---


## Partner Exercise: Create a Music Genre Class

Pair up! Create a new file, `Band.py`.

- Define a class, `Band`, with these instance variables: `"genre"`, `"band_name"`, and `"albums_released"` (defaulting to `0`).
- Give `Band` a method called `display_bio()`, which prints a string like `"The rock band Queen has 15 albums."`
- Store the `genre` in a class variable called `valid_genres` using an appopriate data type, and pre-populate with the genres `rock`, `pop`, and `rap`.
- In the `__init__()` function, if the provided genre isn't in the `valid_genres` collection, print `"Unknown genre"` and set the `genre` variable to `"Unknown"`.

You should be able to create an instance of this class with the following code:

```python
queen = ("Queen", "rock", 15)
queen.diplay_bio()
```


<aside class="notes">

5-10 MINUTES

**Teaching Tips:**

- After students do this, create it and talk through it.
- If you're running short on time, skip an exercise and assign it as homework (the next slide's exercise is more difficult).

**Talking Points:**

- Imagine that you are working with music data of all different types of genres and want to ultimately define three different classes of music (pop, classical, and rock).
- Things to think about:
    * Starting values for variables should be set in the `__init__` method.
    * Class variables are declared inside the class but outside any methods.
    * Instance variables are declared inside the `__init__` method.
    * Does your `__init__` method need to accept any parameters?
</aside>

---

## Partner Exercise: Create a `BankAccount` Class

Switch drivers! Create a new class (and file), `Bank.py`.

Bank accounts should:

* Be created with the `accountType` property (either `"savings"` or `"checking"`).
* Keep track of its current `balance`, which always starts at `0`.
* Have access to `deposit()` and `withdraw()` methods, which take in an integer and update `balance` accordingly.

**Bonus:** Start each account with an additional `overdraftFees` property that begins at `0`. If a call to `withdraw()` ends with the `balance` below `0`, then `overdraftFees` should be incremented by `20`.


<aside class="notes">

10 MINUTES

**Teaching Tips:**

- This is tough! Walk around the room and check for questions and understanding.
- After students do this, create it and talk through it.
- If you're running short on time, skip an exercise and assign it as homework.

**Talking Points:**

- (The same as above.)
- Things to think about:
    * Starting values for variables should be set in the `__init__` method.
    * Class variables are declared inside the class but outside any methods.
    * Instance variables are declared inside the `__init__` method.
    * Does your `__init__` method need to accept any parameters?
</aside>

---

## Knowledge Check

Consider the following class definition for `Cat()`:

```python
class Cat(Animal):
 def __init__(self, name=''):
  self.name = name
  self.fur = short
```

How would you instantiate a `Cat` object with the `name` attribute `'Furball'`?

1. `furball = Cat('Furball')`
2. `furball = Cat()`
3. `furball = Cat(self, name='Furball')`
4. `furball = Cat.__init__(name='Furball')`

<aside class="notes">

**Teaching Tips:**

- Have students guess before telling them.

**Answer:**

1. The `__init__` function is automatically called when creating an object with the `Cat(name='Furball')` syntax.
</aside>

---

## Knowledge Check

Which of the following statements are true about the ```self``` argument in class definitions?

- The user does not need to supply `self` when using instance methods.
- The `self` argument is a reference to the instance object.
- Any variable assigned with `self` (e.g., `self.var`) will be shared across instances of the class.
- With an instance object, `obj`, we can access the variables `var` with the code `obj.self.var`.

<aside class="notes">

**Teaching Tips:**

- Have students guess before telling them.

**Answers:**

1. The user does not need to supply `self` when using instance methods.
2. The `self` argument is a reference to the instance object.

Correct response explanation:

- `self` is automatically passed into an instance method when you call it. `self` refers to the class and NOT the instance. `self.var` will not be shared between instances, as `self` refers to the class. Instances have no explicit `self` attribute.
</aside>

---

## Knowledge Check: Select the Best Answer


Consider the following code:

```python
class Shape(object):
 valid_labels = ['triangle','square','circle','pentagon','polygon','rectangle']

 def __init__(self, label='triangle'):
  self.label = label

 def is_possible(self):
  if self.label in self.valid_labels:
   print('Shape is possible')
  else:
   print('Shape is impossible')

square = Shape(label='square')
wormhole = Shape(label='wormhole')
square.possible.append('wormhole')
```

If you were to enter `wormhole.is_possible()`, would the outcome be `"This is possible"` or `"This is impossible"`?

<aside class="notes">

**Teaching Tips:**

- Have students guess before telling them.

**Answer:**
`This is possible`

Correct answer explanation:

- The possible list is defined at the class level as opposed to as an instance variable. When we append the string `'wormhole'` to the possible list of the `square` object, this list is shared with the wormhole instance. Therefore the output will be `This is possible`.
</aside>

---

## Summary: Discussion

Let's chat! Can anyone explain:

- What a class is?
- What `__init__` does?
- What an object is?
- The point of `self`?
- The two types of variables?


<aside class="notes">

**Teaching Tips:**

- Go through each question and make sure students can explain the answers. Check for understanding!
</aside>


---

## Summary and Q&A

Class:

* A pre-defined structure that contains attributes and behaviors grouped together.
* The blueprint.
* Defined via a method call.
* Contains an `__init__` method that takes in parameters to be assigned to an object.
* E.g., the `Dog` class; the `List` class.

Object:

* An instance of a class structure.  
* The items built from the blueprint.
* E.g., the `gracie` object; the `my_list` object.

---

## Summary: Types of Variables in a Class

Instance variables:

- Contain data types declared in the class but defined in each object.
- Each `dog` has its own name and age.
- Each `my_list` has its own elements.

Class variables:

- Contain data and actions that span across all objects.
- How many `dog` objects are there in total?
- The `self` keyword lets us distinguish between variables that exist at the class level versus in each object.
