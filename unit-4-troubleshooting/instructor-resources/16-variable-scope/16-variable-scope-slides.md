<!--
title: Variable Scope
type: lesson
duration: "00:30"
creator: Brandi Butler
-->

## ![](http://nagale.com/ga-python/images/GA_Cog_Medium_White_RGB.png)  {.separator}

<h1>Unit 3 Lab: Variable Scope</h1>

<!--

## Overview
This lesson introduces local and global scope with a few examples. If there is time, give students examples of broken programs that mix up global and local scopes, and ask them to fix it.

## Learning Objectives
In this lesson, students will:

* Define variable scope.
* Use the global keyword to access global variables.
* Explain the order of scope precedence that Python follows when resolving variable names.


## Duration
20 minutes

## Suggested Agenda

| Time | Activity |
| --- | --- |
| 0:00 - 0:03 | Welcome |
| 0:03 - 0:08 | Local Scope |
| 0:08 - 0:18 | Global scope |
| 0:18 - 0:20 | Summary |

## Differentiation and Extensions
- There are no exercises involving classes, built-in scope, or enclosed scope. If there is time and your students seem confident, create some — or challenge your students to come up with examples themselves.

## In Class: Materials
- Projector
- Internet connection
- Python 3
-->

---

## Lesson Objectives
*After this lesson, you will be able to…*

* Define variable scope.
* Use the global keyword to access global variables.
* Explain the order of scope precedence that Python follows when resolving variable names.

<aside class="notes">

**Teaching Tips:**

- Jot these on the board for reference.

</aside>

---

## Discussion: Delivering a Letter

What if someone wanted to send your instructor Robby a letter?

If you just had "For Robby" the mail carrier would give the letter to the first Robby they see.

Think about how they would go about finding me:

- First in the class. Is there a "Robby" here? They get the letter!
- No? OK, look in the GA Boston Office. Is there a "Robby" here? They get the letter!
- No? OK, look in the entire GA network. Is there a "Robby" here? They get the letter!

<aside class="notes">

**Teaching Tip:**

- Don't mention programming here. Just make sure the class is clear on the idea of scope and how, if we aren't specific, we'll look first in town, then state — continue getting wider.

</aside>  

---

## Discussion: Your Address

This is similar to how variables are looked up.

That's why **scope** matters. We might have to get more specific. To correctly deliver the letter, if the mail carrier only looked in the scope of:

Your class:

- I'm probably the only Robby.
- "For Robby" is fine.

GA Boston:

- There might be multiple Robby's in GA Boston.
- "For Robby, in Classroom 3" is a bit more specific.

Entire GA Network:

- There are multiple Classroom 3's across all GA locations!
- "For Brandi, in Classroom 3 in Boston" is more specific.

---

## Discussion: What Is `x`?

Python has a concept of **scope** as well. We can have many variables with the same name, and Python will look for the most specific one.

Across different scopes, you can reuse the same name. Each one is a *completely different* variable.

Functions and classes each have their own individual **local scope**. A **local variable** doesn't exist outside its local function or class scope.

```python
def my_func1():
  x = 1    # This is a LOCAL variable.
  print(x) # 1

def my_func2():
  x = 5    # This is a DIFFERENT local variable.
  print(x) #5

print(x) # x is OUT OF SCOPE - no x exists here!
```


<aside class="notes">

**Teaching Tips:**

- Walk through this carefully!
- Run it in an interpreter, repl.it, or file to show it working (remove the last `print` to stop the error).
- Terminology is next — just get students to understand the idea.

**Talking Points:**

- Any variable declared or assigned inside of a function is local to that function.
- This is the most specific level of scope and is, ideally, where most of your variables should be declared.
- Only the function in which the variable was declared has access to this scope — i.e., the variable is out of scope for everything but that function.
</aside>  

---

## Global Scope

Variables that are in **global scope** can be accessed anywhere. We define the **global scope** for a specific file as being unbounded to any class or function. 
- Python will check for a local variable before using a global one.

```python
x = 2 # Global to this file

def my_func1():
  x = 1
  print(x) # 1 - Python checks local scopes first.

def my_func2():
  x = 5
  print(x) # 5 - Python checks local scopes first.

my_func1()
my_func2()

print(x) # 2 - Python found no local scope; prints global variable.
```

<aside class="notes">

**Talking Points:**

- If some variables are specifically local, what are the variables outside of a function or class called?
- Any variable declared or assigned outside of any function or class is considered "global."
- Global variables are accessible from anywhere in the script. This is not necessarily a good thing, however, because those variables can be accessed, changed, or reassigned by anything, and this can lead to troublesome bugs.
- This is another case where Python has our backs. It's preventing us from making an accidental error that could easily occur in many other languages.
* Python assumes local unless otherwise specified.
    * Meaning, these `x`s are three different variables.
* Python does this to prevent unexpected behavior and accidental bad practice.
    * It's considered sloppy to have too many global variables.
    * If you have a large code base, you may have forgotten that you used a variable name elsewhere.
    * If you're working on a team, another person may have used a variable name without your knowledge.
</aside>

---

## Multiple Variables, One Name

Use case: `x` and `y` are frequently used to represent numbers.

Scope is important so they don't interact!

```python
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

divide(8,2) # Returns 4
multiply(3,1) # Returns 3
```

<aside class="notes">

**Talking Point:**

- Why would you want to have different variables with the same name? Do you expect each `x` and `y` in this code to perform independently?
</aside>

---

## We Do: Accessing Scopes

Let's start with global scope:

```python
foo = 5
print(foo)
foo = 7
print(foo)
```

<aside class="notes">

**Talking Point:**

- Python makes it a little trickier than other languages to fiddle around with global variables if we're not already in that scope. First, start up a blank script. The following line will assign a global variable named foo the value of `5`. We can easily reassign and access that variable with the following lines. That's the global scope: There's no restriction on accessing or mutating a variable.

**Teaching Tip:**

- Run all the code in these slides in an interpreter for students to see. Encourage them to do this with you.
</aside>

---


## We Do: Accessing Local Scope

What if we add a variable in a local function scope and try to access it from the global scope?

```python
foo = 5

# Delete your other code.
# Add this function and print calls instead.
def coolFunc():
  bar = 8

coolFunc()
print(foo)
print(bar)
```

It fails!

<aside class="notes">

**Talking Points:**

- If you run this code, you will get an error: `NameError: name 'bar' is not defined.`.
- The variable bar is only accessible from inside the `coolFunc()` function.
- We called the `coolFunc()` function, but as soon as it finished running, the variable bar ceased to exist. Even while the function was running, it was only accessible to itself. But, `foo` in the global scope was still accessible.
</aside>

---

## Scope Can Be Tricky

What do you think happened here?

```python
foo = 5
def incrementFoo():
  foo = 6
  print(foo) # prints 6

print(foo) # prints 5
incrementFoo()
print(foo) # prints 5
```

<aside class="notes">

**Teaching Tip:**

- Spend some time here. Ensure student understanding.

**Talking Points:**

- Hey! The variable `foo` went back to its old value after the function finished! Actually, not quite. Here's what happened:
    - The line in the function where `foo` is assigned the value of `6` causes the creation of a new local variable.
    - We then set this variable's value to `6`, the function prints the value, and the function finishes. However, the global variable `foo` was never touched by the function.

**Teaching Tips:**

- Run this!
</aside>

---

## Editing Global Variables

How might we alter the global variable?

```python
foo = 5
def incrementFoo():
  foo = 6
  print(foo) # prints 6
  return foo # returns 6

print(foo) # prints 5
foo = incrementFoo()
print(foo) # prints 6
```

<aside class="notes">

**Teaching Tip:**

- Spend some time here. Ensure student understanding.

**Talking Points:**

- Hey! The variable `foo` went back to its old value after the function finished! Actually, not quite. Here's what happened:
    - The line in the function where `foo` is assigned the value of `6` causes the creation of a new local variable.
    - We then set this variable's value to `6`, the function prints the value, and the function finishes. However, the global variable `foo` was never touched by the function.

**Teaching Tips:**

- Run this!
</aside>

---


## We Do: Global vs. Local

In the following code, there are three `print` statements. Before you run the code, guess what those `print` statements will print.

<iframe height="400px" width="100%" src="https://repl.it/@SuperTernary/python-programming-scope-quiz?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>


<aside class="notes">

**Repl.it Note:**
```
# Global variable x:
x = 1

# Only local x in this function:
def my_func1():
  x = 2 # This is a different, local x
  print(x) # Print the local x

# Using global x:
def my_func2(x):
  print(x)
  x = 3
  return x

my_func1()
x = my_func2(x)

# Print global variable x.
print(x) # Did x get permanently changed by my_func2()?
```
</aside>

---

## Summary and Q&A

Python checks **scope** to find the right variable.

- Functions and classes create individual **local scopes**.
    * A `local` variable doesn't exist outside its local function or class scope.
- Any variable declared or assigned outside of any function or class is considered "global."
    - Variables that are in **global scope** can be accessed anywhere.

Python will check for a `local` variable before using a `global` one.

There can be more levels. Python always works from the inside out — keep that in mind as your programs get more advanced!

<aside class="notes">

**Teaching Tip:**

- Do a check for understanding.
</aside>

---

## Additional Resources

* [Variables and Scope](http://python-textbok.readthedocs.io/en/1.0/Variables_and_Scope.html)
* [Nested Functions — What Are They Good For?](https://realpython.com/inner-functions-what-are-they-good-for/)
