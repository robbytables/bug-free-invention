### ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Python Programming

<!---
This assignment was developed by Brandi

Questions? Comments?
1. Log an issue to this repo to alert me of a problem.
2. Suggest an edit yourself by forking this repo, making edits, and submitting a pull request with your changes back to our master branch.
3. Hit me up on Slack @brandib.
--->

# Python Conditionals: Practice Problems

In this homework, you're going to write code for two challenge problems.

You will practice these programming concepts we've covered in class:

* Declaring and using lists. If you haven't seen the video lecture on lists, [watch it here](https://cl.ly/bd421e98c3f8) 
* Using the Python conditionals `if`, `elif`, and `else`.
* Using `for` and `while` loops.

---

## Deliverables

Part of this homework will be code challenges and part will be reading with comprehension questions.

For the reading questions, make a text file called `answers.txt` and use it to compile your answers to all of the numbered questions.

For each of the code challenges listed below, you will create a new `.py` file and write code to solve the problem. For example, you would create `problem1.py` with your solution code to the first problem. Run the file from the command line to check your work.

*Reminder: On your laptop, you can run the file from your command line with the following:*

```python
python problem1.py
```

> **Hint:** Make sure you are printing something out with the `print` statement, Otherwise, you won't see any output from running your program. But the `print` statement doesn't _return_ values, it just displays them on the console. This is how we can verify the state of our code, by logging information to be displayed.


## Requirements

By the end of this, you should have two different `.py` files (one for each code challenge), and one text file with answers to the five reading comprehension questions.

---

# Code Challenges

## Problem 1: IOU!

### Skill you're practicing: Writing `for` loops to iterate over a list.

You have a list of band names and you want to find out if each of them contain `i`, `o`, or `u` in their names. Loop through each band in the list and print out the following:

```
If the name contains a "u," print out the name plus " rocks!"
Otherwise if the name contains an "i," print out the name plus " should win every award, ever."
Otherwise if the name contains an "o," print out the name plus " is one of the greatest bands of all time."
Otherwise, print the name plus " is super meh."
```

> **Bonus:** Write a function that, given a letter, will return the first band name in the list that contains that letter. If no band name is found, just return "Black Sabbath". They're the greatest band of all time, so it just makes sense to do that. 

#### Starter Code

```python
band_names = ["Rush", "Red Hot Chili Peppers", "Kanye West", "The Ramones", "Wu-Tang", "Beck", "Fleetwood Mac", "Sonic Youth", "Green Day"]

```

#### Expected Output

```
Rush rocks!
Red Hot Chili Peppers should win every award, ever.
Kanye West is super meh.
The Ramones is one of the greatest bands of all time.
Wu-Tang rocks!
Beck is super meh.
Sonic Youth rocks!
Green Day is super meh.
```


> **Hint**: You can determine whether or not a string contains a particular character with an `if` statement. For example, `if "b" in my_string:` will be true if `my_string` contains any b's. The `in` syntax works for lists as well. Test it out - [http://repl.it](http://repl.it)!

---

## Problem 2: If You're Cold, Sit in a Corner. It's 90 Degrees!

### Skill you're practicing: Writing `while` loops.

Wow! It's 90 degrees Fahrenheit and you are sweating buckets! Luckily you have air conditioning, but it's really old and kind of finicky. It cools the room by three degrees and shuts off, so you have to keep turning it back on until the temperature gets to where you want it to be. Seventy five sounds much more pleasant than 90, so that's what you're shooting for.

```
While the temperature is greater than 75 degrees Fahrenheit, print "The temperature is XX — crank the AC!" and subtract 3 degrees from the temperature.

Once the temperature is cool enough and the loop is done, print "75. Ahh, that's better."
```

> **BONUS 1:** When the AC is off, make the temperature climb by 1 degree after every 5th loop. Make sure to wait until the temperature is 78 degrees before you turn the AC back on!

> **BONUS 2:** Create a function containing this logic. Your function should have a meaningful name, and should accept 1 parameter representing the starting temperature. 

#### Starter Code

```python
temperature = 90
```

#### Expected Output

```
Temperature is 90 — crank the AC!
Temperature is 87 — crank the AC!
Temperature is 84 — crank the AC!
Temperature is 81 — crank the AC!
Temperature is 78 — crank the AC!
75. Ahh, that's better.
```

> **Hint:** Make sure that your loop conditional is being updated each iteration. Otherwise you'll end up with an infinite loop!

---

## Reading Material

Read through the examples in these two articles about [`for` loops](https://www.digitalocean.com/community/tutorials/how-to-construct-for-loops-in-python-3) and [`while` loops](https://www.digitalocean.com/community/tutorials/how-to-construct-while-loops-in-python-3) from Digital Ocean. Then, answer the following questions.

1. What is a nested loop? When would you use one?

2. In your own words, what is a `for` loop and why would you use one?

3. In your own words, what is a `while` loop and why would you use one?

4. What is associated the risk involved with `while` loops, and how can it be avoided?

> **SUPER HARD BONUS CHALLENGE:** Write a function `unique_combinations(list1, list2)` , where `list1` and `list2` are both lists of strings, that will create a list of strings representing each unique pairs of strings in each input list.

> For example:

> ```python
> unique_combinations(['a', 'b'], ['c', 'd', 'e'])
> ```

> Will produce the output `['ac', 'ad', 'ae', 'bc', 'bd', 'be']`


---

## All Done!
