<!--
title: Modules and Libraries
type: lesson
duration: "00:40"
creator: Brandi Butler
-->

## ![](http://nagale.com/ga-python/images/GA_Cog_Medium_White_RGB.png)  {.separator}

<h1>Modules and Packages</h1>


<!--

## Overview
This lesson walks through the idea of modules, using the `random` module to look at documentation and methods. Then, it segues into a few longer exercises with PyTime.

## Important Notes or Prerequisites

Libraries were covered extremely briefly in the pre-work (in the Python Introduction lesson), so you can call back to that. They've also used itertools, so you can reference that. This is just a small taste of the many, many modules out there. Highly encourage students to explore more on their own!

## Learning Objectives
In this lesson, students will:

* Add packages and modules to a Python program.
* Create a program utilizing Pytime.
* Navigate library documentation.



## Duration
40 minutes.

### Notes on Timing

It would be easy to get carried away and spend a lot of time either playing around with the modules or reading through the docs. Keep an eye on the clock and move on to the next topic once you've covered a few basic examples. The goal is to understand modules, not to become a pro at any particular one.

### Use the Parking Lot!

Since there are many modules, students may start asking questions along the lines of `Hey, have you used the XXX module?` These are great questions as they reveal a lot of the student's passion and interest! Insofar as possible, try to answer those questions! If you find yourself running short of time, however, write the module name down in the parking lot so you can follow up with that student during a lab or a break.

## Suggested Agenda

| Time | Activity |
| --- | --- |
| 0:00 - 0:03 | Welcome |
| 0:04 - 0:24 | Exploring Modules |
| 0:24 - 0:42 | Pytime Module |
| 0:42 - 0:45 | Summary |

## Differentiation and Extensions
- Don't let slower students be frustrated if they're hung up on a particular function. The main point is that there are other files that they can use that have functions - that's really it.
- For more advanced students, encourage them to experiment with other functions in the modules.

## In Class: Materials
- Projector
- Internet connection
- Python3
-->

---

## Lesson Objectives
*After this lesson, you will be able to...*

* Add packages and modules to a Python program.
* Create a program utilizing PyTime.
* Navigate library documentation.

<aside class="notes">
**Teaching tips**:

- Note that this lesson will be cool! It's easy to be drained after itertools, so stress that this lesson will have easy but awesome things in it.

</aside>

---

## Discussion: Code Reuse

Remember our discussion about Pseudo-Random Number Generators?

Why would we want to recreate those difficult calculations every time we need them?

There must be a better way...

<aside class="notes">
**Teaching Tips**:

- Answer - they're all accomplished with code other people have written for us.
</aside>

---


## What is a Module?

Modules are collections Python code that can be shared, used, and reused throughout applications.

How do we load modules?

* `import <module_name>` at the top of your code- ALWAYS AT THE TOP!
* Then `<module_name>.function_you_want()` when you want to use it.


```python
# import <module_name> - brings in the module file, so we can use it.
import random

# random.randint : "Look in the random module, and use the randint function"
correct_answer = random.randint(0,100)

```

**Discuss:** Why do we need to namespace the `randint` function?


**Pro Tip**: Check the Additional Reading at the end of the lesson to see how to write your own module!


<aside class="notes">

**Teaching Tips**:

- Go through this code - be sure they understand the import
- Ask the students if they think module names are case sensitive

 **Talking Points**:

- "If you recall back to the itertools lesson, you will now see that we are using a module for that extended functionality."

- "A **module**, according to the [Python Docs](https://docs.python.org/3/tutorial/modules.html), "is a file containing Python definitions and statements. The file name is the module name with the suffix `.py` appended."

- You will encounter many modules that others have written. They are free-to-use and you can think of them as extensions of Python's functionality."
</aside>

---

## Python Standard Library

We're going to look at several different modules to get you used to them.


The [Python Standard Library](https://docs.python.org/3/library/) bundles all common modules, so we can just `import` (use) them.


These files are already installed with Python, but aren't loaded into memory autmatically. *Why do you think that is?*

<aside class="notes">
**Talking Points**:

- "This means that they are so commonly used, that they are already included and you don't have to download them separately."
- "There are modules to help with databases, operating systems, logging, data processing, file I/O, and testing, just to name a few!"
- "If you want to use any functions from a module in the standard library, all you need to do is include an import statement for that module at the top of your file."
- "Let's say we're using the random module. We import it; now, we can use the functions in it. Randint returns a random integer between two numbers we give it, including both those numbers."
</aside>

---

## We do: Exploring the Random Module

How do we know:

- What `randint` does?
- What the `random` module has?

Every module has documentation, which has:

- What functions are in the module.
- How to use them.

Here is the <a href="https://docs.python.org/3/library/random.html" target="_blank">documentation for the random module</a>.

- Can you find our `randint` function?


<aside class="notes">

**Teaching Tips**:

- Walk through the documentation, though not in depth - point out the description at the top, that it tells you what module you're in, that it has the functions and brief descriptions. Reminder that they've just seen randint, so point that out.
- End with walking through random, since that's what's next.
- Don't go too in depth in the documentation - introduce the idea of consulting it and the basic idea, but focus on a few simple functions.


**Talking Points**:

- "So, how do we go about using the `random` module now that we know how to include it?"
Let's consult the documentation to get an idea of what functions are available from the random module."
- "There's a lot more functions than you might expect!"

</aside>


---

## Partner Exercise: Random Numbers

Get with a partner and pick a driver! Together:

- Find the `random` function in the <a href="https://docs.python.org/3/library/random.html" target="_blank">documentation</a>. 
- Print out a randomly generated number using `random()`.
- Run the program several times; is your random number different every time?
* Why do you think this is useful?

<iframe height="385px" width="100%" src="https://repl.it/@SuperTernary/Empty-Replit?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

> **Protip**: The `[`, in mathematics means `inclusive`, whereas the `)` means `exclusive`. Thus the possible values include 0.0, but do **not** include 1.0!


<aside class="notes">

3 minutes

**Teaching Tips**:

- After a few minutes, go over the answer.

**Talking Points**:

- "There's a lot more functions than you might expect!"
- "The `[`, in mathematics means `inclusive`, whereas the `)` means `exclusive`. Thus the possible values include 0.0, but do **not** include 1.0!"
</aside>

---

## Quick Review

Modules are collections of useful Python code and functions that we can use.

Use a function by `import <module>` at the top of your code, then `<module>.function_you_want()`.

We've looked at one module: `random`.

```python
# Import statements go at the top of your file
import random

# Using the randint function in the random module
my_random_number = random.randint(2,8)
print(my_random_number)
```

The [Python Standard Library](https://docs.python.org/3/library/) bundles all common modules, so we can just `import` (use) them.

**Next up:** More `random` module practice.


<aside class="notes">

**Teaching Tips**:

- Do a quick check for understanding.

</aside>

---

## We Do: Do You Feel Lucky?


How could you pick a random value from a list? The `random` module has a function called `choice` - it works on any non-empty list.

```python
people_in_lottery = ["Michael", "Soufiane", "Ashish", "Peter", "Tara"]
lottery_winner = random.choice(people_in_lottery)
print(lottery_winner, "wins a new car!")
```

Let's try.

<iframe height="400px" width="100%" src="https://repl.it/@SuperTernary/python-programming-module-chance?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>


<aside class="notes">
**Talking Points**:

- "Let's switch gears a little bit. Random numbers are nice, but sometimes we have a list and we just want to pick a random item on that list. Suppose we run a lottery. We have a list of everyone who bought a lottery ticket and the winner will get a new car. How can we pick a winner?"

**Teaching Tips**:

- Ask the students to change the names to the people sitting around them. If you have a shy class, this gets people talking.
- Try changing the list to hold numbers and other elements.

**Repl.it Note**:
```python
import random

# Directions
# - Replace the names with your name and 4 nearby classmates.
# - Run the program
# - Who won the car?

# Create a list of candidates
people_in_lottery = []

# This is selecting one winner
lottery_winner = random.choice(people_in_lottery)

# This announces the winner!
print(lottery_winner, "wins a new car!")
```
</aside>

---


## Partner Exercise: Let's Get Random!

Get with a partner and create a local file, `random_cards.py`

- Generate a random number with `random.randrange()`. Print it out.
- Create a list of cards, like `cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king", "ace"]`
- Use `random.shuffle()` to mix up your deck; print that out.
- Use `random.choice()` to deal a random card in your deck. Print it out.
- **BONUS:** Create a function that can take an integer argument corresponding to the number of cards to deal. Make sure each card can only be dealt once per function call.

Here is the <a href="https://docs.python.org/3/library/random.html" target="_blank">documentation for the random module</a>, so you can look up functions.

<aside class="notes">

5 minutes

**Teaching Tips**:

- They'll need to look in the documentation to see shuffle; we haven't gone over it. This is a good exercise to get them used to looking at docs.
- Walk around and see if there are questions.
- Go over the  answer when time's up or you feel it's time to do so - walk  through finding `shuffle` in the docs as well.

</aside>


---


## Quick Review

Modules are collections of useful Python code and functions that we can use.

Use a function by `import <module>` at the top of your code, then `<module>.function_you_want()`.

The [Python Standard Library](https://docs.python.org/3/library/) bundles all common modules, so we can just `import` them. `random` is a module inside the Python Standard Library.

```python
# Import statements go at the top of your file - they import straight from the Python Standard Library!
import random

# Using the randint function in the random module
my_random_number = random.randint(2,8)
print(my_random_number)

chained_list = list(itertools.chain(food, colors))
```

**Up Next**: What about modules that *aren't* in the standard library?


<aside class="notes">

**Teaching Tips**:

- Do a quick check for understanding.

</aside>

---

## What are Modules and Packages?

* A Module is a Python file
* Each Module contains structures and functionality for a single utility
* A Package is a collection of Modules
* Packages are bundles of diverse solutions centered on some common goal
* Package == Library

The [Python Standard Library](https://docs.python.org/3/library/) bundles all common modules - it's the package with the `random` module inside it.


<aside class="notes">
**Talking Points**:
- "Both `library` and `package` are technically correct and we can use the terms interchangeably."
- "PyTime is an interesting example of a package, because it only has one module in it"
</aside>

---

## External Modules: PyTime


The Python Standard Library has a [huge list](https://docs.python.org/3/library/index.html) of modules. But not every Python module in the world is part of it!

`pytime` is a non-standard module. PyTime can:

* Get dates, date ranges, and times.
* Find the date of a particular holiday.

PyTime is *not* in the PSL.

<aside class="notes">

**Teaching Tips**:

- Have them open a file and run this with you. If they protest that it's just one line, note that you'll be building on it.

**Talking Points**:

- "Of course, not every module or package out there is part of the standard library. Those that are more industry-specific such as `numpy` for data science, `flask` for web development, or `pygame` for game development are excellent tools for you to use. They just aren't included because not everyone uses them."

- "ModuleNotFoundError happens when you try to use a module that doesn't exist. This  could  be because it isn't installed or it actually doesn't exist - maybe you made a typo. In any case, Python  can't find it!

</aside>

---


## Including PyTime

If you're importing from the Python Standard Library, you can just import the module directly.

```python
# (implied: from standard_library) import <package>
import random
```

Otherwise, you have to specify the package from which you want to import the module.

```python
# from PACKAGE import MODULE
from pytime import pytime

# The names won't always be the same:
from pygame import joystick
```


Some good reading on this:

* [Stack Overflow Answer #1](https://softwareengineering.stackexchange.com/questions/187403/import-module-vs-from-module-import-function/187471)
* [Stack Overflow Answer #2](https://stackoverflow.com/questions/710551/use-import-module-or-from-module-import)


<aside class="notes">

**Teaching Tips**:

- Have them do this with you. For them, it won't work - it's not installed.

**Talking Points**:

- "Because pytime is a package, we need to import the pytime module FROM the pytime package. It's a little confusing because they have the same name! But as you'll see in a moment, in the code itself, one is a folder name and the other is a file name."
- "You can see with joystick and pygame that modules and packages don't need to have the same name."
</aside>


---

## Installing PyTime


New packages that aren't in the Python Standard Library (AKA PSL AKA Pumpkin Spice Latte) need to be installed.

Let's install `pytime`.

First, find it on [PyPi](https://pypi.org/project/pytime/)

Now, in your **command prompt**:

```
pip3 install pytime
```

Once that's successful, import `pytime` in a file called `module_practice.py`.

> **Protip**: `pip` stands for `Pip Installs Packages`. `pip3` uses Python3.


> Note: Repl.it is a great website for testing, because it has all Python packages _ever_ already installed.


<aside class="notes">

**Teaching Tips**:

- Make sure they all successfully install pytime and run their file.
- Students might get stuck on `pip` - walk around the room to be sure they've all installed pytime successfully. Consider they might need `python3 -m pip install pytime`
- Bring up a blank repl.it to show that you can test modules without needing to install them. Repl.it is great for this! (https://repl.it/@SuperTernary/Empty-Replit?lite=true)

**Talking Points**:

- "If we want to use `pytime` in repl.it, it will automatically download it for us. How nice!"
- PIP3: "**Note**: Remember `pip` stands for `Pip Installs Packages`. This helps us download and use the modules/packages we need. The `3` just makes sure we're using Python 3!"
</aside>

---

## PyTime Holidays

Let's explore PyTime:

- Scan the <a href="https://github.com/shinux/PyTime" target="_blank">PyTime docs</a>, to find the `mother` function.

When is Mother's Day?

```python
from pytime import pytime

# This gets mother's day of 2016
mothers_day = pytime.mother(2016) # 2016-05-08
```

What about the current year?

```python
# This gets mother's day of this year
mothers_day = pytime.mother()
```



<aside class="notes">
Teaching tip:

- Open the docs with the students and pick out mother's day to explain. Encourage discussion on the docs.

**Talking Points**:

- "Let's explore the PyTime docs together."
- "To start out, let's just focus on the holidays"
- After Examples: "**Note**: It turns out that pytime defaults to the current date when there are no arguments provided."
- Before Going to Next Slide: "Looking through the documentation, we see uses of `father` and `easter` functions. They work the same way as `mother` where you may provide a `year` as an argument or let it default to the current year."
</aside>

---

## Quick Review

Not all modules are in the standard library. If you try to import a module Python doesn't recognize, you'll get a `ModuleNotFoundError`.

When importing from the standard library, the package is implied:

```python
# (from standard) import MODULE
import random
```

Otherwise, you need to specify the package!

```python
# from PACKAGE import MODULE
from pytime import pytime
from pygame import joystick
```

If you're using a non-standard package like `pytime` or `pygame`, you'll have to also install it.

You can use the website repl.it for testing small pieces of code - it has packages installed.

**Up next**: Continuing exploring documentation.

<aside class="notes">

**Teaching Tips**:

- Do a quick check for understanding.

</aside>


---

## You Do: PyTime Festivals

Look through the <a href="https://github.com/shinux/PyTime" target="_blank">PyTime docs</a>; can you find the `father` and `easter` functions?

In your local file, create a variable holding your date year as an integer. In that year, print the month and day of:

* Mother's Day.
* Father's Day.
* Easter Sunday.



<aside class="notes">

5 minutes

**Teaching Tips**:

- Give students a chance to do this on their computers.
- Then, go over it - point out the functions in the documentation.

</aside>


---

## We Do: The Grinch Who Stole Christmas?

Why does the documentation only have 3 holidays?

Time for some sleuthing! Most times, you only need to look at a module's documentation. However, sometimes the person that did the documenting didn't write everything down.

Because a module is simply a `.py` file, we can view it.

- Open up the project's [Github page](https://github.com/shinux/PyTime).
- Look at the files and folders near the top of the page.
- Click on the folder `pytime`.
- Click on the file `pytime.py`.
- Scroll down to the `Festivals` section at the bottom of the file.
- What function do you see which would likely give you Christmas Day?


<aside class="notes">
**Teaching Tips**:

- Start a discussion here - see if students can figure out how to solve this on their own. Give reminder hints that a module is just a python file filled with functions.
- Show examples of a couple other holidays, such as Valentine's Day
- Be sure everyone understands what they've done here.

</aside>

---

## Summary and Q&A

Modules are `.py` files with functions. They're written by other people for us to use!

- A package (a.k.a. library) is a bundle of one or more modules.
- Python's standard library has a lot of common modules! `random`, `itertools`, etc.
- Nonstandard libraries need to be installed (`pip3 install pytime`).

To use modules, at the top of your file, put:

```python
# From the standard library: `import MODULE`
import random

# From non-standard packages: `from PACKAGE import MODULE`
from pytime import pytime
from pygame import joystick

# And preface your function with the module name.
mothers_day = pytime.mother(2016) # 2016-05-08
```

<aside class="notes">

**Teaching Tips**:

- Do a summary check for understanding.
- If questions are not forthcoming, see if students can describe the random and pytime modules in their own words. Pop quiz!

</aside>

---

## Additional Resources

* [Python Modules](https://docs.python.org/3/tutorial/modules.html)
* [Python's Standard Library](https://docs.python.org/3/library/index.html)
* [Write a module in python 3 - Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-write-modules-in-python-3)
* [Itertools](https://docs.python.org/3/library/itertools.html)
* [Random](https://docs.python.org/3/library/random.html)
* [PyTime](https://pypi.org/project/pytime/)
* [List of Commonly Used Packages](https://pythontips.com/2013/07/30/20-python-libraries-you-cant-live-without/)
* [Useful Modules by Discipline](https://wiki.python.org/moin/UsefulModules)
* [Further Reading](https://www.learnpython.org/en/Modules_and_Packages)
* [Formatting Datetime](https://docs.python.org/3.0/library/datetime.html#strftime-behavior)
