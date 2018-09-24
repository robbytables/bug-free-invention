### ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Python Programming

<!---
This assignment was developed by Cody.

Questions? Comments?
1. Log an issue to this repo to alert me of a problem.
2. Suggest an edit yourself by forking this repo, making edits, and submitting a pull request with your changes back to our master branch.
3. Cody isn't in GA, so hit me up on Slack instead at @zoe.lubitz.
--->


# Unit 5 Lab: Finalizing the Movie App

## Overview

This is the lab we've been working toward. Here, you'll add an API call to actually get the Rotten Tomatoes rating, prompt a user for whether they want to search for a movie or view a rating, and read in an API key from a file.

We'll be using the <a href="https://www.omdbapi.com/" target="\_blank">OMDb API</a>.

It's a long lab, but it's going to be worth it. Buckle up — here we go!


------------

## Deliverables

You're going to continue building this locally from the last lab. You'll write all of your code in the same `movie_app.py` file.

Run the file from the command line to check your work.

Additionally, you will have a file, `omdb-api-key.txt`, with your *own* OMDb API key.

## Requirements

In addition to the previous `print` statements, your app prompts a user for a `1` or a `2`, calls an API, and does one action accordingly:

- Inputting `1` when the program starts searches for a movie:

    ```
    > ./main.py
    Search (1) or Ratings (2)? 1
    Enter a search term: back to the future
        Back to the Future
        Back to the Future Part II
        Back to the Future Part III
        Ivan Vasilievich: Back to the Future
        Back to the Future... The Ride
        Back to the Future
        Back to the Future: Making the Trilogy
        Back to the Future: The Game - Episode 1, It's About Time
        The Secrets of the Back to the Future Trilogy
        Back to the Future: The Game - Episode 5, Outatime
    ```

- Inputting `2` when the program starts prints the Rotten Tomatoes rating:

    ```
    > ./main.py
    Search (1) or Ratings (2)? 2
    Enter the movie title: Back to the Future
    The rating for "Back to the Future" is 96%.
    ```
---


## Directions

Augment the code you wrote for the Unit 2 lab.

### Part 1: User Input

**Part 1a: Search or Rating Prompt**

Let's start with the simplest part — having a user input `1` or `2`.

1. Delete the `search_or_ratings` declaration at the top of your file — you won't need it.

1. At the top of your `while` loop in `main`, create the `search_or_ratings` variable. Set it equal to the `input` of the prompt, `"Would you like to search for a movie (1) or find the rating of a specific movie (2)?"`

1. Remember that `input` always returns a string, so either typecast it to `int` or change your `if` block accordingly.

**Part 1b: Movie Title Prompt**

We want the user to search for a movie, not always print our hard-coded value.
1. In the `if` and `elif` blocks, prompt a user with `"Enter the movie title: "` and save the input into a new variable, `movie_query`.
    - Food for thought: Why do you think we put two separate `movie_query` prompts versus one above the `if` block?

1. Let's now use this title. If the user inputs `2`, the app calls `  print_single_movie_rating("Moana")`. Change this argument to be the user's input. Test it out!

1. `list_search_results()` is eventually going to do just that — list the search results for the user's input! We don't have the search functionality yet, so right now let's just prep for it by passing in the user's input as well as `default_movie_list`.

### Part 2: Prepping for the API

**Part 2a: Adjusting Existing Code**
1. For this API to work, you'll need a few libraries. At the top of your code, add these lines:
  ```python
  import urllib
  import json
  from urllib.parse import urlencode
  from urllib.request import urlopen
  ```

2. Next, you'll need to sign up for an API key. It's free!
      - Go to <a href="https://www.omdbapi.com/apikey.aspx" target="_blank">this URL</a>.
      - Follow the prompts and you'll get a key that looks something like this: `eraa00e882` (that one's not real — don't use it!). Test out your API key by putting this URL in your browser: `https://www.omdbapi.com/?apikey=[your key]&t=moana`.
      - It returns quite a lot! But, pulling out a few key pieces: The very first thing is the `Title`, which we'll need. Near the end, right after the poster URL, you can see the `Ratings` — it's a `Source : Value` dictionary, exactly like you already have.

3. Let's make the key available to your program. Save this key in a file called `omdb-api-key.txt` in the same folder as your `movie_app.py`.
      - Now that it's in a file, let's create a function that reads it in. Create a function called `get_apikey()`.
      - In it, open `omdb-api-key.txt`, `read` the contents, and save the result into a variable, `key`.
      - Then, use `.strip()` to strip any whitespace characters and `print` out the key.
      - Call `get_apikey()` from `main` so you can see it working (but once you've verified, delete the call).

4. Let's prepare our `Movie` class for this. When we create `Movie` objects, we'll be passing in this block of OMDb data as `movie_data`. Let's make our variables a little more descriptive.
      - Where you have `self.movie_data = movie_data`, change that to `self.omdb_data = movie_data`. Change the getters accordingly.
      - In `get_movie_rating()`, change the default for the `source` parameter to `"Rotten Tomatoes"`.
      - Remember that capitalization matters! We have a lowercase `title` and `rating` right now, but in the API the dictionary keys are `Title` and `Ratings`. Change yours in the two getter functions.
    - Your movie class is set! You can minimize it — we won't be changing it again in this lab.


**Part 2b: Applying Programmatic Thinking**

1. Before we add the API, let's apply some programmatic thinking. Where should we put the API call? What needs to call the API?
    - `list_search_results()` is going to need to call the API to find the search results. Follow along: Let's pseudocode out what we need to do and mark it with `TODO` so we don't forget.

    ```python
    # Because we're going to get the list by searching, this function should only take in the `movie_query`.
    def list_search_results(movie_query):
        """
        Print list of movies. Later, print a list of title results from a movie search.
        """

        # TODO: All below.

        # To call the API, we'll need the API key.
        # Call `get_apikey()` and save it as `apikey`.

        # Then, we'll need to make an API client to call the API. We'll also need to search for the actual movie. This might look something like:
        # omdb_results = OMDB_call(apikey, movie_query)
        # But, we aren't really sure until we actually call the API.
        # When we do make this, we should probably put it in a try/except block in case the API call fails.

        # Once we have our results, we can loop through them and print them.
        # We know from the example call on the website that each movie object is a dictionary with a "Title" key. We can use list comprehensions to make a list from this. If we save it in `movie_titles`, we don't need to change the `for` loop below, and we can delete the list parameter in the function declaration:
        # movie_titles = [each_movie["Title"] for each_movie in matching_movie_list]


        # Loop through list of titles and print them (indented with four spaces).
        for title in movie_titles:
            print("    " + title)
    ```

    - In preparation for this, change the call to `list_search_results()` to only have the `movie_query`.

    - Also, change `get_apikey()` to `return` the key instead of printing it. `get_apikey()` is now done — you can minimize it!

1. Where else will we need to call the API? `return_single_movie_object()` literally returns the `Movie` object given a movie title, so probably there. Let's think about it:
    1. Once again, because we're getting the movie data from the API call, we only need the movie title passed in. Take off the `movie_rating` parameter; look through the rest of the code for any calls to `return_single_movie_object()` and make sure they're only passing in a title.
      1. Once you've done this, you can minimize the functions `print_all_ratings()` and `print_single_movie_rating()`. We're done with them!
      1. While we're at it, you can minimize `main`. We're done with that, too! You're making great progress.

    1. Continuing, let's think about `return_single_movie_object()`. How does it compare to `list_search_results`? Let's pseudocode it out:

    ```python
    # Because we're looking up the movie, we don't need to pass in the rating. Let's change the other parameter from "movie_title" to "movie_query" so it's more clear that we haven't looked it up yet.
    def return_single_movie_object(movie_query):
    """
    Take in the movie title and rating, and return the movie object.
    """
    # TODO: All below.

    # To call the API, we'll need the API key.
    # Call `get_apikey()` and save it as `apikey`.

    # Then, we'll need to make an API client to call the API. We'll also need to search for the actual movie. This might look something like:
    # omdb_results = OMDB_call(apikey, movie_query)
    # But, we aren't really sure until we actually call the API.
    # When we do make this, we should probably put it in a try/except block in case the API call fails.

    # Once we have our movie from the API result, we can make a `Movie` object out of it and return that. Something like this, but we're not really sure yet:
    # return Movie({"title": omdb_result[Title], "rating": omdb_result[Ratings]})
    ```

We've done everything we can in preparation. We know where we need the API (`return_single_movie_object()` and `list_search_results()`), and we have a general idea in pseudocode of what we're going to do with the results, so let's actually call it.

### Part 3: Calling the API

**Part 3a: Creating the API Class**

Before we do anything, put this code at the top of your file, right underneath the `import` calls:
```python
class OMDBError(Exception):
    """
    OMDBError represents an error returned by the OMDb API.
    """
    pass
```

Now, for the API. Let's put the API calls in a class. This way, we can keep all the API-related methods in one place, and it's easy for any other function to call.

What methods might our class have?
- We'll certainly need an `__init__`.
  - In it, we can set the API key as an instance variable.
- To call an API, we need the URL we're calling. We'll have a `build_url()` method.
  - The parameters will be anything we want to put in the URL. We'll use `**kwargs`, as we won't know what they are in advance.
- Lastly, we'll want to actually call the API — we'll have a `call_api()` method.
  - This will get called by outside functions and therefore will call `build_url()`. We'll need to take in the `**kwargs` as a parameter here to be able to pass them on.

Let's get to it!

1. Create a class, `OMDB(object)`. Put it near the top of your file, right under the `Movie` class, so all of your methods are available in the rest of the file.
  1. Take in `apikey` and set `self.apikey = apikey`. (Do you remember where?)

1. In the class, create a method, `build_url()`, that takes in an arbitrary number of keyword arguments (`**kwargs`), builds the URL, and returns the URL to call the API.
    - Use the code below, but make sure you understand it:
    ```python

      def build_url(self, **kwargs):
          """
          build_url returns a properly formatted URL to the OMDb API including the
          API key.
          """

          # Add API key to dictionary of parameters to send to OMDb.
          kwargs["apikey"] = self.apikey

          # Start building URL.
          url = "http://www.omdbapi.com/?"

          # urlencode the API parameters dictionary and append it to the URL.
          url += urlencode(kwargs)

          # Return the complete URL.
          return url
        ```

1. Next, let's make a `call_api()` method, which, as the name implies, actually calls the API. It takes in `**kwargs` as well — these will be the search parameters to send to the API, such as the name of the movie we're searching for.
      1. The first thing it does it call `build_url(**kwargs)` and saves that into a `url` variable.
      1. Next, it should open the URL (using `urlopen(url)`) and save that into a `response` variable.
      1. Then, `read()` that response and save it into `response_data`. Now we have some JSON with all of the movie information.
      1. Let's use `json.loads()` to decode the `response_data` and save that into a variable called `response_data_decoded`.
      1. Before we continue, let's error-check! Add this code under your `response_data_decoded` declaration:

        ```python
        # Check for an error and throw an exception if needed.
        if "Error" in response_data_decoded:
          raise OMDBError(response_data_decoded["Error"])
        ```

      1. Then, return `response_data_decoded`, so that whatever called the API now has access to the movie information.

**Part 3b: Using the API Class**

At this point, what do you think we should do?
- We have a way to call the API, so we could go use this in `return_single_movie_object()` or `list_search_results()`.
- However, what if, in the future, we want to get a list of search results or a single movie's information and not anything else that's in those functions?
- Let's make more class methods to handle this.

1. Let's create a method in our OMDb class that calls gets a single movie's info that `return_single_movie_object()` can call.
    1. Create a method called `get_movie()` that takes in a `movie_query` parameter — this is what `return_single_movie_object()`, or any other function in the future, will pass to it.
    1. In it, set a variable `movie_data` to the return of `self.call_api` with (`t=movie_query`) as an argument. The "t" here stands for "Title."
    1. Take the `movie_data` that's returned and create a `Movie` object out of it. Return that `Movie` object.

1. Let's check out our `return_single_movie_object()` and see if we can do something about this pseudocode.
  1. First, let's call the API key and save it in `apikey`. That's straightforward — we had that already!
  1. Next, we have this pseudocode existing in our function:

        ```
        # Then, we'll need to make an API client to call the API. We'll also need to search for the actual movie. This might look something like:
        # omdb_results = OMDB_call(apikey, movie_query)
        # But, we aren't really sure until we actually call the API.
        # When we do make this, we should probably put it in a try/except block in case the API call fails.
        ````

  1. However, most of this is done in our class. Let's make an OMDb object from the class, passing in our API key, and save it as `omdb`.
  1. Next, let's get that `Movie` object. Call `omdb.get_movie(movie_to_look_up)` and save it as `my_movie_object`.
  1. Return `my_movie_object`.
  1. We're almost good to try it out! Let's add an error check in case it fails. Wrap your `omdb` call in a `try`/`except` block, like this:

```python
# Get `Movie` object. If OMDb error occurs, print the error message and exit.
try:
    my_movie_object = omdb.get_movie(movie_to_look_up)
    return my_movie_object
except OMDBError as err:
    print("OMDB Error: {0}".format(err))
    return
```

**Break: Let's Test!**

At this point, we can try it out!
- We'll need to comment out any calls to `list_search_results()`, because we haven't done anything in that function yet (the only one is in `main`).
- Now, try running it! Before you even input anything, the `print` statements at the beginning should run:

  ```
  The movie Back to the Future has a rating of 96%
  The movie Blade has a rating of 54%
  The movie Spirited Away has a rating of 97%
  ```
  Then, inputting `2` and entering "Moana" should return a ratings result of 97% (remember, capitals matter!).

If your program hangs (doesn't respond) for more than a minute, hit `ctrl-c` to stop it. If you get stuck, try troubleshooting it, then ask for help.

**Moving on: Let's Add Search!**

This is the last bit! Great job. How cool is your app so far?

- In the class, add a `search()` method.
  - Like `get_movie()`, take in a `movie_query`.
  - Call the API, but have the argument be `s=movie_query`; the "s" here stands for "search." Save the result in a variable called `movie_dictionaries`.
  - Then, return the value of the `Search` key of that dictionary.

That's it for the OMDb class! Let's do the final piece, which is `list_search_results()`. This function is going to look very similar to `return_single_movie_object()`. The few differences are:
- In `list_search_results()`, instead of calling `.get_movie`, call `.search` and save the result in a variable, `matching_movie_list`.
- Below the API call and above the `for` loop, uncomment the list comprehension from the pseudocode.

Test this out by uncommenting the call to `list_search_results()` in `main`, then searching for `Blade`.

If you get stuck, ask for help!

That's the end! Amazing job.
