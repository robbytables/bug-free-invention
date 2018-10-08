<!--
title: Further Data Structures
type: lesson
duration: 00:40
creator: Steve Peters
-->

## ![](http://nagale.com/ga-python/images/GA_Cog_Medium_White_RGB.png)  {.separator}

<h1>Python Programming: Sets and Tuples</h1>

<!--

## Overview
This lesson focuses on sets and tuples. It starts with sets, encompassing  We Dos as new functions are introduced, then goes into tuples. It ends with the `type` function and a You Do. If there's time, after the "Additional Reading" slides, there is a sets exercise. This exercises are also in the `xx-additional-exercises` folder, if you don't get to it.

## Important Notes or Prerequisites
- The students will be asked to build upon their knowledge of the `list`, so a solid understanding of this concept will be vital.
- The "why" of each datatype is essential to impart to students and your checks for understanding may keep circling back around to the "why".
- Much of this lesson contrasts the three data types (tuples, sets, lists) to each other, so that students can see them side by side and start to internalize the differences.

## Learning Objectives
In this lesson, students will:

- Perform common actions with sets.
- Perform common actions with tuples.
- Know when to use each of the different collection structures.


## Duration
40 minutes

### Timing note:
- If there's time remaining at the end, giving exercises involving multiple contrasting sets, tuples, and lists would be great.
- There is, in the `xx-additional-exercises` folder in the parent folder, a set equals challenge that you should give in class if there's time, and if not, give as homework.

## Suggested Agenda

| Time | Activity |
| --- | --- |
| 0:00 - 0:02 | Welcome |
| 0:02 - 0:20 | Sets |
| 0:20 - 0:37 | Tuples |
| 0:37 - 0:40  | Summary |

## In Class: Materials
- Projector
- Internet connection
- Python3
-->

---

## Learning Objectives

*What are we learning in this lesson?*

- What are sets and how do we use them?
- What are tuples and how do we use them?

<aside class="notes">

**Teaching Tips**:

- Quickly overview these; perhaps write them on the board.

</aside>

---

## Discussion: Lists


What's wrong with this list?

```python
subscribed_emails = ["mary@gmail.com", "opal@gmail.com", "mary@gmail.com", "sayed@gmail.com"]
```



<aside class="notes">

**Talking Points**:

- "Why, in the `subscribed_emails` list, would duplicate entries be a problem? Or unique colors having duplicates?"

**Teaching Tips**:

- You can guide students to think about deduplication and the need to ensure unique values, thus dovetailing into sets

</aside>

---

What issues could arise from duplicates in a list?

What have we learned recently that could help eliminate the problem of duplicates in a list?


---

## Introducing Sets


Lists:
```python
subscribed_emails = ["mary@gmail.com", "opal@gmail.com", "mary@gmail.com", "sayed@gmail.com"]
print(subscribed_emails)
# -> ["mary@gmail.com", "opal@gmail.com", "mary@gmail.com", "sayed@gmail.com"]
```

Sets: Lists without duplicates!
```python
subscribed_emails = {"mary@gmail.com", "opal@gmail.com", "mary@gmail.com", "sayed@gmail.com"}
print(subscribed_emails)
# -> {"mary@gmail.com", "opal@gmail.com", "sayed@gmail.com"}
```

- Notice the `[]` versus the `{}`.

<aside class="notes">

**Talking Points**:

- Refresh memories that a *list* is a collection of *elements*, contained within square brackets `[]`:

- "However, there is a specific version of a *list* called a *set*. What makes a set different is that all of the *elements* in a *set* must be unique. That is to say, nothing can appear more than once in a *set*." Sets have curly braces.

</aside>


---


## How Can We Make a Set?


Making a set via a list - Python removes duplicates automatically.

```python
my_set = set(a_list_to_convert)

# In action:
product_categories = ["shirts", "pants", "shirts", "jackets", "socks", "shirts"]
product_categories = set(product_categories)
# => {"shirts", "pants", "jackets", "socks"}

# Instead of passing a list in (a_list_to_convert), we could just type it:
product_categories = set(["shirts", "pants", "shirts", "jackets", "socks", "shirts"])
# => {"shirts", "pants", "jackets", "socks"}
```

Making a set directly, in curly braces:

```python
colors = {"red", "orange", "yellow", "green", "blue", "indigo", "violet"}
```

<aside class="notes">

**Talking Points**:

- "Creating a *set* is easy; we just need to use the `set()` method like this."

- "Because we had two `red`s, Python removed the extra one for us."

**Teaching Tips**:

- Point out the difference between parentheses, brackets, and curly braces.

</aside>


</aside>

---

## Important Note: Sets

Lists are always in the same order:

- `my_list = ["green", "yellow", "red"]` is always going to be`["green", "yellow", "red"]`
- `my_list[0]` is always  `"green"`; `my_list[1]` is always `"yellow"`; `my_list[2]` is always `"red"`.

Sets are not! Like dictionaries, they're in any order.

- `my_set = {"green", "yellow", "red"}` could later be `{"red", "yellow", "green"}`!
- `my_set[0]` could be `"green"`, `"red"`, or `"yellow"` - we don't know!

We **cannot** do:  `print(my_set[0])` - it could be anything! Python won't let us.

---

## We Do: Creating a Set from a List

Let's pull up a new `set_practice.py` file and make some sets!

- Make a list `clothing_list` containing the main color of your classmates' clothing.
- Using `clothing_list`, make a set named `clothing_set`.
- Use a `for` loop to print out both `clothing_list` and `clothing_set`.
- Try to print an index!

<aside class="notes">

**Teaching Tips**:

- Run through this with them - make sure they are following along to practice typing the syntax.
- Be prepared to refresh memories on `for` loops.
- Try to print an index - reinforce that sets are in any order.

</aside>

---

## We Do: Adding to a Set

How do we add more to a set?

```python
# In a list:
clothing.append("red")

# In a set
clothing.add("red")
```

Think About It...
- Why is the function `add` rather than `append`?
- What happens if you add a duplicate?

<aside class="notes">

**Talking Points**:

- Continue locally with the list and set they created previously - do this with them!
- Try to add a duplicate, then print. Call out that it just doesn't appear, since sets can't have duplicates.

</aside>

---

## We Do: Removing from a List and a Set

Since lists are always the same order: 
- `colors = ["green", "yellow", "red"]`
- `colors[0]` is always "green".

and sets are not:

- `colors = {"green", "yellow", "red"}`
- `colors[0]` could be `green`, `red`, or `yellow`.

Removal of items behaves much differently. The `pop` function cannot be called without any paramters, as there's no guarantee as to the identity of the 'first' item in a set.
Instead, the `pop()` function must consume the _key_ of the entry to be removed.

```python
# In a list:
colors.pop() # Removes and returns the last item in the list.
colors.pop(0) # Removes and returns a specific (here, the first) item in the list.

# In a set
colors.pop() # No! This is unreliable! The order is arbitrary.
colors.pop(0) # No! Python throws an error! You can't index sets.
colors.remove('red') # Do this! Call the element directly!
```

<aside class="notes">

Teaching points:

- Walk through these. `pop` from the set to show that it's unreliable.

**Talking Points**:

- Address that for lists, the order matters. For sets, it's irrelevant, so `pop` returns an arbitrary element.
- Discuss the difference between `remove` and `pop`.

</aside>
---

## Quick Review: Sets vs. Lists

**Lists**:

- The original, normal object.
- Created with `[]`.
- `append()`, `insert(index)`, `pop()`, `pop(index)`.
- Duplicates and mutable.

**Sets**:

- Lists without duplicates.
- Created with `{}` or with `set(my_list)`.
- `add()` and `remove(element)`.

<aside class="notes">

**Teaching Tips**:

- A code review for all of these are on the next slide.
- Review these - on this slide, do a check for conceptual understanding.
</aside>

## Quick Review: Sets vs. Lists

```python
### Creation ###
# List
colors_list = ["red",  "yellow", "green", "red"]
# Sets
colors_set = {"red",  "yellow", "green"}
print(colors_set)

# Set From List
colors_set2 = set(my_list)
print(colors_set2)

### Appending a New Value ###
colors_list.append("blue")
colors_set.add("blue")

### Appending a Duplicate ###
colors_list.append("blue")
# => colors_list = ["red",  "yellow", "green", "red", "blue",  "blue"]
my_set.add("blue")
# => colors_set = {"red",  "yellow", "green", "blue"}

### Removing items: ###
colors_list.pop(1)
colors_set.remove("red")
```

<aside class="notes">

**Teaching Tips**:

- Do a quick check for understanding.
- Go through each example.

**Talking Points**:

- Point out again the difference in syntax, especially with curly braces.
- Reinforce `pop` being unreliable.

</aside>

---

## Discussion: Immutability Thoughts

A set is a type of list which doesn't allow duplicates.

What if, instead, we have a list we don't want to change?

```python
rainbow_colors = ("red", "orange", "yellow", "green", "blue", "indigo", "violet")
```

We **don't** want:
```python
rainbow_colors[0] = ("gray")
## Gray's not in the rainbow!
rainbow_colors.pop()
## We can't lose violet!
rainbow_colors.append("pink")
# Pink's not in the rainbow!
```

We want `rainbow_colors` to be **immutable** - meaning the values in the list _cannot_ be changed.


<aside class="notes">

**Talking Points**:

- We're done with sets.
- Immutable means "unchangeable".

</aside>

---

## Introducing: Tuples


**Tuples** are another core collection type.

- Duplicates, but immutable.
- A list that _cannot_ be changed.

```python
rainbow_colors = ("red", "orange", "yellow", "green", "blue", "indigo", "violet")
```

When should you use a tuple?

- Tuples should be used whenever multiple items of information need to be coupled together, and remain unchanged throughout their lifetime
- One example would be pairs of (x, y) coordinates

<aside class="notes">

**Talking Points**:

- Point out that with tuples, duplicates are fine! Be clear that tuples are another kind of list, NOT a kind of set.
* Python offers a data structure that provides more secure usage than the wide power of a fully mutable list.
* The **tuple** is a kind of data structure that provides immutable values in a list.
* Once a tuple is created and assigned its elements, no changes can be made to the tuple.
* "Why? Isn't it more useful to work with a list that allows us to change elements when necessary? Doesn't this inflexibility make our code easier to break?
- "We will frequently need the power to create and edit lists, adding and removing items from them. In these instances, use a list."
</aside>

---

## Tuple Syntax

- Created with parentheses `()`.
- Access values via numerical indices (similar to lists).

```python
rainbow_colors = ("red", "orange", "yellow", "green", "blue", "indigo", "violet")
print(rainbow_colors[1])
# Prints "orange"
```

- Tuples can be iterated over with a `for` loop, just like a set or list

```python
for color in rainbow_colors:
  print(color)
```

<aside class="notes">
**Talking Points**:

- Tuples work exactly like lists, except that, when you create a tuple, you use parentheses instead of square brackets.
- You can include anything you want, but, for now, we'll add strings.

</aside>

---

## We Do: Tuples

Let's declare a tuple named `seasons` and set it to have the values `fall`, `winter`, `spring`, and `summer`. We'll print the tuple and each value. Then we'll try to reassign them (we can't)!

<iframe height="400px" width="100%" src="https://repl.it/@SuperTernary/Empty-Replit?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

<aside class="notes">

**Teaching Tips**:

- Make sure they're doing this with you.
- Print out each value directly with indexes. Then, use a `for` loop.
- Try to change values - pop, append, and direct reassignment.

Talking point:

- Remind them of the syntax - perhaps make sets and lists as well, so students can see them compared again.

</aside>

---

## Quick Review: Sets, Tuples, Lists

**List**:
`["red", "red", "yellow", "green"]`
- Ordered collection of values
- Allows duplicates 
- Mutable: `append()`, `insert(index)`, `pop()`, `pop(index)`

**Set**:
`{"red", "yellow", "green"}`.
- Unordered collection of unique values
- No duplicates!
- Mutable: `add()` and `remove(element)`

**Tuple**:
`("red", "red", "yellow", "green")`
- Immutable collection of ordered values
- Allows duplicates
- Items cannot be added, removed, or altered in any way

<aside class="notes">

**Teaching Tips**:

- A code review for all of these are on the next slide.
- Remind them about `add` vs `append` - this is because we can't guarantee it's going at the end!
- Review these - on this slide, do a check for conceptual understanding.
- Always reinforce the `[]` vs `{}` vs `()`
- Recap immutability.
</aside>

---

## Quick Review: Sets, Tuples, Lists

```python
### Creation ###
# List
color_list = ["red",  "yellow", "green", "red"]
# Sets
color_set = {"red",  "yellow", "green"}
color_set2 = set(color_list))
# Tuples
color_tuple = ("red",  "yellow", "green")

### Appending a New Value ###
color_list.append("blue")
color_set.add("blue")
# Tuples -> You can't!

### Removing items: ###
color_list.pop(1)
color_set.remove("red")
# Tuples -> You can't!
```

<aside class="notes">

**Teaching Tips**:

- Do a check for understanding of the code syntax.
- Go through each example.

**Talking Points**:

- Recap the types of braces to create each; remove vs pop; append vs add.
- Remind students that they aren't expected to be syntax experts - they can always look this up. Working programmers look things up every day on the job, but students have to know what things are and what to expect.

</aside>

---

## Introducing Types

Variables certainly can hold a lot!

- Sets, tuples, and lists are easily confused.
- `type()` tells us what a variable is: set, tuple, list, dictionary, integer, string - anything!

Try it:

<iframe height="300px" width="100%" src="https://repl.it/@SuperTernary/python-programming-types?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>


<aside class="notes">

**Talking Points**:

- It's useful to know what datatype a variable is and how to use it. This will work on anything.

**Teaching Tips**:

- Walk through each of these. It will recap the syntax as well as re-inforce using `type`. You might want to open the repl.it in a new window, as it's a bit long.


**Repl.it Note**: This replit has:
```python
unique_colors = set(["red", "yellow", "green", "red"])
print("unique_colors is", type(unique_colors))
# --
unique_colors_2 = ["red", "yellow", "green", "red"]
print("unique_colors_2 is", type(unique_colors_2))
# --
unique_colors_3 = ("red", "yellow", "green", "red")
print("unique_colors_3 is", type(unique_colors_3))
# --
my_number = 2
print("my_number is", type(my_number))
# --
my_string = "Hello!"
print("my_string is", type(my_string))
```

</aside>

---



## Summary and Q&A

We've learned two new types of lists:

Sets:

- A mutable list without duplicates.
- Handy for storing emails, usernames, and other unique elements.

```python
email_set = {'my_email@gmail.com', 'second_email@yahoo.com', "third_email@hotmail.com"}
 ```

Tuples:

- An immutable list that allows duplicates.
- Handy for storing anything that won't change.

```python
rainbow_tuple = ("red", "orange", "yellow", "green", "blue", "indigo", "violet")
```

---

## Additional Reading

- [Repl.it that recaps Tuples](https://repl.it/@SuperTernary/python-programming-tuple-practice?lite=true)
- [Python Count Occurrences of Letters, Words and Numbers in Strings and Lists-Video](https://www.youtube.com/watch?v=szIFFw_Xl_M)
- [Storing Multiple Values in Lists](https://swcarpentry.github.io/python-novice-inflammation/03-lists/)
- [Sets and Frozen Sets](https://www.python-course.eu/sets_frozensets.php)
- [Sets](https://www.learnpython.org/en/Sets)
- [Python Tuple](https://www.programiz.com/python-programming/tuple)
- [Tuples](http://openbookproject.net/thinkcs/python/english3e/tuples.html)
- [Strings, Lists, Tuples, and Dictionaries Video](https://www.youtube.com/watch?v=19EfbO5D_8s)
- [Python Data Structures: Lists, Tuples, Sets, and Dictionaries Video](https://www.youtube.com/watch?v=R-HLU9Fl5ug)

---

## Partner Exercise: Equal Sets

Pair up! Pick a driver.

For two sets to be equal, they simply have to contain the same elements - it doesn't matter what order they're in.

Unfortunately in Python, comparing two sets using `==` will only produce `True` if the elements are in the same order - not what we want!

Write a function that takes two sets and returns `True` if they have the same elements, even if they aren't in the same order.

For example, the second test fails. Your function would instead return `True`.

```python
fruits = ['orange', 'pear', 'kiwi', 'apple', 'banana']

fruits_copy = ['orange', 'pear', 'kiwi', 'apple', 'banana']

fruits_reordered = ['pear', 'apple', 'kiwi', 'orange', 'banana']

print("Copy comparison", fruits == fruits_copy)
print("Reordered comparison", fruits == fruits_reordered)
```
