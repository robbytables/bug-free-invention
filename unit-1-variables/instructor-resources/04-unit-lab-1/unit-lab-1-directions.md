
<!---
This assignment was developed by Sonyl

Questions? Comments?
1. Log an issue to this repo to alert me of a problem.
2. Suggest an edit yourself by forking this repo, making edits, and submitting a pull request with your changes back to our master branch.
3. Hit me up on Slack @sonylnagale.
--->
## ![](http://nagale.com/ga-python/images/GA_Cog_Medium_White_RGB.png)  {.separator}

<h1>Unit 1 Lab: Variables</h1>

---

## Overview
Welcome to the first unit lab!

Throughout the course, there is a lab at the end of each unit. Each lab builds upon the last.

At the end of Unit 5's lab, you will have built an app that asks the user to enter a movie title. Your app will then search for that movie on <a href="https://www.rottentomatoes.com/" target="\_blank">Rotten Tomatoes</a> and print the search results and the Rotten Tomatoes rating.

For example, if a user searches in your app for "Blade", your app can get a list of results: "Blade," "Blade II," "Blade Runner," "Blade Runner 2049," and "Blade of the Immortal (Mugen no jûnin)." Your app can also tell the user that *Blade* has a 54% rating on Rotten Tomatoes.

It's going to be awesome!

Right now, let's set up some variables and print out their values.

---

## Deliverables

You're going to build this locally on your computer.

1. Create a new folder on your Desktop called `movie_rating_lab`. That folder is where we'll keep all the files we create for our unit labs.

1. Create a `.py` file called `movie_app.py`. You'll write all of your code in this file.

Run the file from the command line to check your work.

*Reminder: On your laptop, you can run the file from your command line with the following command:*

```python
python movie_app.py
```

**Hint:**

Make sure you're printing something out with the `print` statement! Otherwise, you won't see any output from running your program.


## Requirements:

By the end of this, you will have a `movie_app.py` file that prints out:

`The rating for Back to the Future is 8`.

---


## Directions

Our first goal is just to get the app printing out movie titles and ratings. We'll hard-code in some values for now.

1. Create a variable `movie_title` and set it to `Back to the Future`.
1. Create a variable `movie_ratings` to hold the rating and set it to `8`.
1. Make a `print` statement that says, `The rating for <movie_title> is <movie_rating>`. It should call your new variables, so for example, the string `The rating for Back to the Future is 8` should not appear in your code, rather, it should be built from the variables you've created.
