<!--
title: Next Steps in Web Development
type: lesson
duration: "01:00"
creator: Kevin Coyle
-->

## ![](https://s3.amazonaws.com/python-ga/images/GA_Cog_Medium_White_RGB.png)  {.separator}

<h1>Templates</h1>

---

## Learning Objectives
*After this lesson, you will be able to:*

- Create a template HTML document.
- Pass variables to a template HTML document via a Flask app.

---

## A Million Copies

- Don't you hate it when you have to repeat yourself?

- What if you had a website with 10 pages that were almost the same?

- Would you code them all from scratch?

---

## Templating

<aside class="notes">

**Teaching Tip:**

- Talk for a few minutes here about design patterns and why it's important to split data from presentation.
</aside>

We use templates to:

- Write one HTML file.
- Pass it variables.
- Transfer info from Flask to HTML.

As well as for one important design reason:

- We can separate data from how we present data to users.

---

## Jinja2

- One of the most widely used template engines for Python.
- One of the two main modules that comprise Flask's basis
---

## Why Jinja2?

<aside class="notes">

**Talking Points:**

- Jinja2 is kind of like the engine that powers our vehicle (Flask). However, this happens behind the scenes.
- We're quickly peering behind the scenes to get an idea of what our engine can do.

- Some examples of what makes Jinja2 awesome are:
  - **Template inheritance:** You can extend templates in very efficient ways.
  - **HTML escaping:** Malicious hackers can create XSS attacks by injecting HTML code into our site where other users insert data. Jinja2 helps us avoid that.
  - **Speed and efficiency:** Jinja2 is very fast. It compiles optimized Python code.
  - **Flexibility and extensibility:** It's really easy to add our own filters and functions.
</aside>

Jinja2 has some really powerful features that web design folks want to take advantage of:

- Template inheritance
  - Like class inheritance!
- HTML escaping
  - Stops some hacking attacks (XSS and SQL injection).
- Speed and efficiency
  - Optimized Python code.
- Flexibility and extensibility
  - We can add our own filters and functions.


---

## We Do: Templating

Let's create two endpoints that render the same HTML file
	
Try the following:

```
@app.route('/anna_1')
def anna_1():
  return render_template('annas_site.html')

@app.route('/anna_2')
def anna_2():
  return render_template('annas_site.html')
```

- What if we want them to display a different heading?
- Do we need to duplicate the whole file?

---

## Templating Annas Site

- We'll send a `name` variable into our `annas_site.html` from both routes.

- The routes will display different things!

---

## Adding Templates

<aside class="notes">

**Talking Points:**

- This is the function that Flask uses to… you guessed it: Render our template(s)!
- For this exercise, we want to add some programming language (Python) into our HTML template.
</aside>

- Remember `import render_template`?
- This is the function that Flask uses to… you guessed it: Render our template(s)!

---

## Edit `index.html`

- Replace `Anna Smith` with a `{{ name }}` variable in the `<h1>` at the top of our site.

```html
...
   <body>
      <h1>{{ name }}</h1>
	....
```

---

## Templating Syntax With Jinja

<aside class="notes">

**Talking Points:**

- What's awesome about this is that inside of these brackets, we can pass in Python syntax.
- In our example, we have a variable, which we're calling `name`.
- Whatever we assign to the variable `name` will be rendered when our page renders.
- Statements are where we would pass in logic like {%if this thing%} {% else that thing%}.
</aside>

- Recognize the `{{ }}`?

- In Jinja, **templates** are rendered with double curly brackets (`{{ }}`).

- **Statements** are rendered with curly brackets and percent signs (`{% %}`).

  - A use case here is passing in logic like:
	```python
	{% if name == 'kevin' %}
	# Do the thing
	{% else %}
	# Do all the other things.
	```

---

## Rendering a Template in Flask

<aside class="notes">

**Talking Points:**

- We're going to modify the rest of our Flask app to pass some values into our variable in the template (curly braces).
- Let's change the rest of our `hello_flask.py` so that the whole thing looks the following script on screen.

- Here, we use `render_template` function which takes in two arguments:
  1. Our template name, `index.html`.
  1. Our **context** which, from the documentation is "the variables that should be available in the context of the template."

- Here, our variable is name which is passed into the <user> part of our route, and then becomes the value that we assign to the variable called `name`.
</aside>

Let's change our `my_website.py` accordingly:


```
@app.route('/anna_1')
def anna_1():
  return render_template('annas_site.html', name="Robby Grodin")

@app.route('/anna_2/<name>')
def anna_2(name):
  return render_template('annas_site.html', name=name)
```
---

## Try it!

- Check out: `http://localhost:5000`.
- Then: `http://localhost:5000/anna_1`
- And: `http://localhost:5000/anna_2`

Do your other routes still work?

---

## Your Turn!

- Create a new Flask app, `blog.py`.
- Create a new template HTML file, `post.html`.
- Now create a text file called `first_post.txt`, in the same directory as your `blog.py` file.
- Create an `blog_post()` function, and give it the route `@app.route('/post')`
- Create an HTML file with a single `<p>` tag in the body, with the content being `{{ post }}`.
- Render the template with the body of the blog post text file provided to the template.
- Launch your Flask app and check the results!

---

## Template Solution

```html
<!doctype html>
<html>
<head>
    <meta charset="utf-8">
    <title>Blog Post</title>
</head>
<body>
    <p>{{post}}</p>
</body>
</html>
```

---


## Python Solution

```python
from flask import Flask, render_template

app = Flask(__name__)


with open('first_post.txt') as file:
	text = file.read()

@app.route('/post')
def blog_post():
    return render_template("post.html", post=text)

if __name__ == '__main__':
	app.run(debug=True)
```



---

## Summary

- Jinja:
  - A popular templating engine.
  - Templates save us time and abstract presentation from data.

- Template fun:
  - We can pass variables into the template from the Flask app and the URL.
