<!--
title: Variables and Routing in Flask
type: lesson
duration: "01:00"
creator: Kevin Coyle
-->

## ![](https://s3.amazonaws.com/python-ga/images/GA_Cog_Medium_White_RGB.png)  {.separator}

<h1>Variables and Routing in Flask</h1>

---

## Learning Objectives
*After this lesson, you will be able to:*

- Create a route in Flask.

---

## Routing

<aside class="notes">

**Talking Points:**
- By now, you may be wondering about that `@app` that we put on the line before our index function.
  - `@` annotations are calls "decorators"
  - A decorator is a way to put one Python function into another Python function.
  - More formally, this process is called "wrapping a function" inside of another function.
  - You can check out more on decorators later, but for now, knowing that our `@app.route("/")` is a way that we pass an argument — the endpoint — into a routing function.
  - In other words: We tell our Flask app to listen to a particular endpoint and then we have a function that gets called if that endpoint gets hit.
</aside>

We have:

- Listen to an endpoint (here, `/`).
- Do `def index()` if someone goes there.

```python
@app.route('/') # When someone goes here...
def index(): # Do this.
  return "Hi!"
```

`http://127.0.0.1:5000/`
`=> "Hi!"`

What if we want to go to `http://127.0.0.1:5000/about`?

---

## Suddenly, a New Page!

- This is **routing**.
- New pages on our web app!

```python
@app.route('/about') # When someone goes here...
def hello(): # Do this.
	return "All about me!"
```

---



## What Is a Route?

<aside class="notes">

**Talking Points:**

- A route is an endpoint
- In the context of a website, a route delivers a webpage
- The endpoint we pass into the route function becomes part of the URL
</aside>

- The base URL: `http://127.0.0.1:5000/`
- We *route* to different URLs:
	- `http://127.0.0.1:5000/about`
	- `http://127.0.0.1:5000/portfolio`
	- `http://127.0.0.1:5000/contact`

- `about`, `portfolio`, `/`, and `portfolio` are **endpoints** from our main app.

- We only need to add:

	```python
	@app.route('/<endpoint>') # When someone goes here...
	def function_name(): # Do this.
		return string
	```

---

## You Do: Adding a Route

- In `my_website.py`, add a new route to a `randnum` endpoint.
- In the function for this endpoint, display a string that's a random number.
	- *Hint:* Remember the `random` module? You can use `randint(1, 100)`.
	- *Hint:* You can turn an integer to a string with `str(number)`.

- Reload the page and go to your endpoint to try it out!


<aside class="notes">
**Current Code Status**:

```python
from flask import Flask, render_template
import mySecrets ## You can import any file!
import python_variables
import os # Note the new import — to be in the file system.
import random

app = Flask(__name__)

## Call it like a module.
my_name = mySecrets.username
my_password = mySecrets.password

student_name = python_variables.student_name

file_path = '.'

with open(os.path.join(file_path, 'more_variables.txt')) as f:
	the_text = f.read()

@app.route('/text')
def read_txt():
	return the_text

@app.route('/') # When someone goes here...
def home(): # Do this.
    return render_template("index.html")

@app.route('/about') # When someone goes here...
def hello(): # Do this.
    return "Hello, Mr. Fieri."

@app.route('/randnum')
def randnum():
    return str(random.randint(1, 100))

if __name__ == '__main__':
	app.run(debug=True)


```
---


## Variables in the Route

- You can pass a variable in the route itself.
- It's a dynamic endpoint!
- You can use that variable in your function.

```python
@app.route('/about/<name>')
def about(name):
	return "Who's a good dog? " + name + " is a good dog!"
```

`http://localhost:5000/about/Yuki`
`=> Who's a good dog? Yuki is a good dog!"`


<aside class="notes">
**Current Code Status**:

```python
from flask import Flask, render_template
import mySecrets ## You can import any file!
import python_variables
import os # Note the new import — to be in the file system.
import random

app = Flask(__name__)

## Call it like a module.
my_name = mySecrets.username
my_password = mySecrets.password

student_name = python_variables.student_name

file_path = '.'

with open(os.path.join(file_path, 'more_variables.txt')) as f:
	the_text = f.read()

@app.route('/text')
def read_txt():
	return the_text

@app.route('/') # When someone goes here...
def home(): # Do this.
    return render_template("index.html")

@app.route('/about/<name>')
def hello(name):
	return "Hello, " + name + ", your coding skills impress me!"

@app.route('/randnum')
def randnum():
    return str(random.randint(1, 100))

if __name__ == '__main__':
	app.run(debug=True)
```

---

## Your Turn!

Try adding route in your Flask app to have:

- A `/timesfour/<number>` route that displays the product of an integer in the route multiplied by four.
- A `repeat` route that takes a string passed into the URL, then displays it four times in a row.

---
