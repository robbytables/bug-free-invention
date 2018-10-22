<!--
title: Scripting
type: lesson
duration: "00:35"
creator: Brandi Butler
-->

## ![](http://nagale.com/ga-python/images/GA_Cog_Medium_White_RGB.png)  {.separator}

<h1>Python Programming: Scripting</h1>


<!--


## Overview
This lesson starts with an explanation of a scripting language vs a compiled language, then goes on to discuss the idea of a script. The majority of the lesson is spent teaching file I/O, with just a couple slides near the end for user input.


## Learning Objectives
In this lesson, students will:
* Explain the uses of scripting.
* Write scripts that perform file I/O.
* Write scripts that take user input.

## Duration
35 minutes.

### Notes on Timing

It would be easy to get carried away and spend a lot of time covering all the tiny pieces of file I/O. There are many slides that introduce terms, such as `with` or `append`, so that students won't be lost if they later find them in a tutorial online. Spend very little time here - enough to ensure the student conceptually understands the concept. They don't need to actually practice it.

## Suggested Agenda

| Time | Activity |
| --- | --- |
| 0:00 - 0:03 | Welcome |
| 0:04 - 0:08 | Introducing Scripting |
| 0:08 - 0:24 | File I/O |
| 0:25 - 0:32 | User Input |
| 0:32 - 0:35 | Summary |


## In Class: Materials
- Projector
- Internet connection
- Python3
-->

---

## Lesson Objectives
*After this lesson, you will be able to...*

* Explain the uses of scripting.
* Write scripts that perform file I/O.
* Write scripts that take user input.

---

## What's a Scripting Language?

There are two main categories of programming languages in the world: **interpreted languages** and **compiled languages**.

Interpreted Languages are also known as Scripting Languages.

Scripting languages:

* Python
* PHP
* BASIC
* Javascript

Compiled Languages:

* Java (sometimes)
* C++
* C
* Lisp

---

## What's a Scripting Language?

Compiled languages:

* Compile means "build".
* Compilation is the process of building a machine runnable file
* More steps between coding and running, but tend to run faster
* Customized to run in a specific environment

Interpreted Languages:

* Are ran in a "virtual machine", can be run in any environment
* Faster iterations between coding and running, but runtime tends to be slower
* Are ran line by line, errors are found when they happen

You don't need to memorize this - just know that there's a difference.


<aside class="notes">

**Teaching Tips**:

- It's not important for them to memorize what compiled is - just get the idea that it's a different kind of language.

**Talking Points**:

* A `scripting language` or interpreted language like Python executes statements in order
* A `script` is typically a file with some Python code in it
* A script might calculate something, take input, give output, or do file I/O

All programming languages that exist  in the world fall into one of two buckets. A `scripting language` or interpreted language like Python executes statements in order. A compiled language needs to build your program before running it.

Imagine; you wrote an application with Java. Before  you can run it, you need to compile it - turn it  After compiling completed, you run your application. When running your application, you notice a bug. To fix it, you have to stop your application, go back to source code, fix the bug, wait for the code to recompile, and restart your application to confirm that it is fixed. And if you find another bug, you’ll need to repeat that process again.

In a scripting language, you can fix the bug and just need to reload your application —no need to restart or recompile anymore. It’s as simple as that.

Technically, you've been writing scripts already.

</aside>

---

## What is a Script?

Code that automates a task.

Can be as simple or as complex as needed!

Let's write a script:

```python
print("hello world!")
```

**CONGRATS**: You now have a script!

Look familiar? You've been scripting since day 1!

<aside class="notes">
**Talking Points**:

It turns out, you already know how to do this!
</aside>

---

## Scripting, Commonly

When people say scripts, though, they usually mean code that:

* Takes input.
* Gives output.
* Reads or writes to a file.
* Performs a task.

We have "perform a task" down!

<aside class="notes">
**Talking Points**:

All Python files you write are scripts! But when people say scripts, that's not really what they mean.
</aside>

---

## Scripting, Part 1: Files

Let's further our programming toolkit.

On your computer, you can:

- Create or open a file (text, jpg, Word doc...).
- Read it.
- Edit it.
- Close it.

Anything a user can do on a computer, Python can do as well.


<aside class="notes">

Teaching tip:

- This is to get them to conceptually understand what we're about to do - don't mention code here.

</aside>

---

## We Do: Let's Read a File!

With files, there are three key points.

1. Tell Python to open the file: `file = open(<file name>)`
2. Do something with the file! (Read it, edit it, etc).
3. Close the file when you're done: `file.close()`

Let's try this out.

1. Create a file called `message.txt`, and put a secret message in there.

2. Now, also on your Desktop, create a file, `file_reading_script.py`.  Fill it with:
    ```python
    file = open("hello.txt")
    print(file.read())
    file.close()
    ```
3. Run it!

**Note:** The file must exist already!


<aside class="notes">

**Teaching Tips**:

- Do this with them.
- Make sure they successfully make the .txt file and have all successfully run the code.

</aside>


---

## What About Editing Files?

In Python, "edit" is referred to as "write", short for "write to." How do we write a file?

`open(<file name>)` has optional parameters: `open(<file name>, <mode>)`

- Mode: "What do you want to do with the file?" The default is "read." Use `w` for "write":

#### File Modes
| Value  | Name  | Details  |
|---|---|---|
| 'r' | Read  | Read only, can't change contents  |
| 'a' | Append  | Can write but only to the end of the file  |
| 'w' | Write  | Able to edit file freely  |
| 'r+' | Read + Write | Can read and write to/from the file |
---

## We Do: Writing Files

Let's write the value of a variable to our file.

```python
# Open the file
file = open("message.txt", "w")

# Write some content
file.write("Hello bartender")
text = "I'll take a Whiskey."
file.write(text)
file.write("Have a nice day!")

# Always close the file!!!!!!!!!!!
file.close()
```

Run it!

Open the file to check.

**Thought:** How could you make new lines?

<aside class="notes">

**Teaching Tips**:

- Do this with them.
- Make sure they have all successfully run the code.
- Have them talk about making new lines - they've learned `\n` previously.
- If you think they can handle it, give them a few reasons to always close the file.

</aside>

---


## We Do: Creating Files

What if the file doesn't exist yet?

**Write** to the rescue!

* Write opens a file for writing...
* But it also creates it if need be!

Try this:

```python
# Open OR create file
new_file = open("totally_new_file.txt", "w")

# Write some content
new_file.write("Content goes here")

# Always close the file
new_file.close()
```

Check your desktop after running it!


<aside class="notes">

**Teaching Tips**:

- Do this with them.
- Make sure they have all successfully run the code.

</aside>

---

## Let's try: Copying a File

Let's try doing the following:

1. Read in the contents of a file
2. Write those contents to a new file
3. Make sure to close all open files!!

<aside class="notes">

3 minutes

**Teaching Tips**:

- After they do this, show it to them. Show them opening multiple files at the top, too, so they know you don't have to go sequentially: e.g.

```python
file_to_read = open("a_file.txt")
file_to_write = open("file_script.txt", "w")


string_to_write = file_to_read.read()
file_to_write.write(string_to_write)

file_to_read.close()
file_to_write.close()
```
</aside>

---

## Quick Review

You can open, read, and write files with Python.

Write will create the file if it doesn't already exist.

Always close your files!

```python
file_to_read = open("a_file.txt")
file_to_write = open("file_script.txt", "w")


string_to_write = file_to_read.read()
file_to_write.write(string_to_write)

file_to_read.close()
file_to_write.close()
```

**Next up:** More advanced file options.

<aside class="notes">

**Teaching Tips**:

- Do a quick check for understanding.

</aside>

---



## I Do: The With Keyword

Always remembering to close a file can be hard.  There's another way to open files so Python closes it for us!

```python
# Instead of:
file = open("file.txt", "w")
file.write("Hello World!")
file.close()

# We can say:
with open("file.txt", "w") as file: # This introduces a block that will automatically close the file when it's exited
  file.write("Hello World!") # Note the indent!
````


<aside class="notes">
**Talking Points**:

* As you can see, file I/O is associated with a lot of potential errors.
* Sometimes if a file doesn't close properly, this can lead to:
    * Memory pollution on your computer
    * Keeping a file in use when it isn't
* These are bad problems! Luckily, Python has our back once again with `with`!
* `With` shortens our code, catches errors gracefully, and makes `close` unnecessary.

**Teaching Tips**:

It's not necessary they become experts in this. Just show it to them so that they're aware if they  find  it in a tutorial.
Here is a repl.it, if you'd like:
https://repl.it/@brandiw/03-Python-Scripting-03
</aside>

---

## What Else is in File?

These are just for reference - we won't be using them!

For future reference: [Documentation on File I/O](https://docs.python.org/3/tutorial/inputoutput.html)

- Do you have a list of strings that you want to write on multiple lines? Use `file.writelines([<your list>])`

- Does your file have things on multiple lines you want to read into a list variable? Use `list_contents = file.readlines()`

- Separating some written lines? Add `\n` to the `write()`

<aside class="notes">
**Teaching Tips**:

- If you have time (remember, user input is still coming), open a file and show these in action.
- It's not essential for students to know, but it's good for them to see.
- Skim this slide quickly if students are starting  to look lost.

Here is a repl.it, if you'd like:
"https://repl.it/@brandiw/03-Python-Scripting-01
</aside>

---

## Quick Review:

File has a lot of advanced options.

- You can write a list across multiple lines, or read a file with multiple lines into a list variable.
- Write only takes one argument, so concat your strings!
- You can open files using `with` to automatically close them.


**Next up:** User Input!

---

## What about User Input?

We've just done a lot with file I/O (in/out).

We can prompt users for information, too.

You've seen this a few times, it's very common in scripting to allow finer grained control.

```python
# Prompts with "input"
# Saves result in user_name
user_name = input("Please type your name:")
```

<aside class="notes">
**Teaching Tips**:

- Run this! Show this a few ways. Try type casting the input to an int.

Here's a repl.it, if you'd like:
https://repl.it/@brandiw/03-Python-Scripting-04?lite=true
</aside>
---

## You Do: Bring it all together!

1. Create a file called `about.py`.
2. In it, prompt the user for their name. Then, prompt them for their favorite food.
3. Using write, create a file called `about_me.txt`.
3. In `about_me.txt`, write out the name and favorite food in a sentence.

**Bonus**: Use `format` for forming your sentence!


<aside class="notes">
5 minutes

**Teaching Tips**:

- After students give this a shot, show the answer.
- If there's still time, show a few variations of this with other things we've covered, like append and `with` to open.
</aside>

---

## Summary and Q&A

Scripting language vs compiled language.

- Scripting languages: Write -> Run.
- Compiled languages: Write -> Build -> Run.

Script:

- Just some code!

---

## Summary and Q&A

File I/O:

- `file = open("a_file.txt", "w")`
- `file.write("Some content")`
- `file.write(my_text)`
- `file.close()`

User input

- `user_name = input("Please type your name:")`


<aside class="notes">

**Teaching Tips**:

- Check for understanding; review key concepts.

**Talking Points**:

*We accomplished quite a bit!*

* Defined what a script means contextually.
* Showed how to open and close a file on your computer.
* Discussed different modes of opening files.
* Wrote a script that accepted a user's input
</aside>

---

## Additional Resources

* [Socratica Video: Text Files](https://www.youtube.com/watch?v=H_R5yRtFtuc)
* [Executing a Python Script](https://www.python-course.eu/python3_execute_script.php)
* [Reading and Writing Files](http://www.pythonforbeginners.com/files/reading-and-writing-files-in-python)
* [File Object Documentation](https://www.tutorialspoint.com/python3/python_files_io.htm)
* [Binary vs Text Files](https://www.nayuki.io/page/what-are-binary-and-text-files)
