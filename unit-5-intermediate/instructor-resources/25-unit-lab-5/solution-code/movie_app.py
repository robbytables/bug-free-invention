import requests

class OMDBError(Exception):
    """
    OMDBError represents an error returned by the OMDb API.
    """
    pass

class Movie(object):
    """
    `Movie` objects contain all information about a particular movie,
    including the title and rating.
    """

    def __init__(self, movie_data):

        # Store the raw data from OMDb in this object so that we can use the
        # data in the getter functions.
        self.omdb_data = movie_data

    def get_movie_title(self):
        """
        `get_movie_title` is a getter function that returns the movie title.
        """

        # Return the title from the movie data.
        return self.omdb_data["Title"]

    def get_movie_rating(self, source="Rotten Tomatoes"):
        """
        get_movie_rating is a getter function that returns the rating.
        """

        # There can be multiple ratings for each movie, so they are stored as a
        # list of ratings, each with a source and a rating. By default, we are
        # only interested in Rotten Tomatoes ratings, so we loop through each
        # rating and return it if the source is Rotten Tomatoes.
        for ratings in self.omdb_data["Ratings"]:
            if ratings["Source"] == source:
                return ratings["Value"]

        # If the code makes it here, it hasn't returned in the `for` loop.
        return "- Wait - Rating for source {0} was not found!".format(source)

class OMDB(object):
    """
    OMDb objects represent clients to the OMDb API. It has helper methods for
    performing functions on the API.
    """
    def __init__(self, apikey):
        # Store the API key so it may be used later to build the authenticated URL.
        self.apikey = apikey
        self.url = "http://www.omdbapi.com/?"

    def call_api(self, **kwargs):
        """
        `call_api` uses the provided parameters to create a URL to the OMDb API,
        call the API, parse the results, and return the parsed JSON data.

        If the API returns an error, the error is raised as an exception.
        """

        # Add the API key to the dictionary of parameters to send to OMDb.
        kwargs["apikey"] = self.apikey

        # Call the API by requesting the URL. Use `json()` to decode the raw JSON data.
        response_data = requests.get(self.url, kwargs).json()

        # Check for an error and throw an exception if needed.
        if "Error" in response_data:
            raise OMDBError(response_data["Error"])

        # Return the decoded data.
        return response_data

    def get_movie(self, movie_query):
        """
        Get a `Movie` object containing all the data for a single movie. Returns
        a single `Movie` object.
        """
        # Call the API, passing the movie_query as "t" (by title).
        movie_data = self.call_api(t=movie_query)

        # Create a `Movie` with the raw results from the API call.
        return Movie(movie_data)

    def search(self, movie_query):
        """
        Search for movies based on keywords. Returns list of dictionaries.
        """
        # Call the API, passing the movie_query as "s" (by search).
        movie_dictionaries = self.call_api(s=movie_query)

        # Return the list of movie dictionaries.
        return movie_dictionaries["Search"]

def get_apikey():
    """
    Read API key from file on disk.
    """

    # Open file in read mode (r).
    with open("omdb-api-key.txt", "r") as file:

        # Read the file into a variable (key).
        key = file.read()

        # Strip any whitespace characters such as a newline that may be present
        # in the file.
        key = key.strip()

        # Return the key.
        return key



def list_search_results(movie_to_look_up):
    """
    Prompt for search term and print list of matching movies.
    """

    # Read the API key from disk.
    apikey = get_apikey()

    # Create OMDb client with the provided API key.
    omdb = OMDB(apikey)

    # Get results from the OMDb API. If OMDb error occurs, print the error message and exit.
    try:
        matching_movie_list = omdb.search(movie_to_look_up)
    except OMDBError as err:
        print("OMDB Error: {0}".format(err))
        return

    # Extract titles from the search result list with list comprehension (each
    # result is a dictionary).
    movie_titles = [each_movie["Title"] for each_movie in matching_movie_list]

    # Loop through the list of titles and print them (indented with four spaces).
    for title in movie_titles:
        print("    " + title)



def return_single_movie_object(movie_to_look_up):
    """
    Prompt for movie title and return the movie object.
    """

    # Read the API key from disk.
    apikey = get_apikey()

    # Create OMDB client with the provided API key.
    omdb = OMDB(apikey)

    # Get `Movie` object. If OMDb error occurs, print the error message and exit.
    try:
        my_movie_object = omdb.get_movie(movie_to_look_up)
        return my_movie_object
    except OMDBError as err:
        print("OMDB Error: {0}".format(err))
        return

def print_single_movie_rating(movie_query):
    """
    Create a `Movie` object and print one movie's Rotten Tomatoes rating.
    """

    my_movie = return_single_movie_object(movie_query)

    # Print the rating. Note that we have to escape the quotes around the movie
    # title because those quotes are inside a string that also uses quotes.
    print("The rating for \"{0}\" is {1}.".format(my_movie.get_movie_title(), my_movie.get_movie_rating()))

def print_all_ratings(movie_list):
    """
    Take in a list of movies, create a `Movie` object for each, and print the rating.
    """

    for movie in movie_list:
        movie_object = return_single_movie_object(movie)
        print("The movie", movie_object.get_movie_title(), "has a rating of", movie_object.get_movie_rating())


# Create one main function that will call everything else.
def main():

    """
    Main is the entry point into the program, and it calls into the search or
    ratings functions depending on what the user decides to do.
    """

    # A hard-coded movie list to test with.
    default_movie_list = ["Back to the Future", "Blade", "Spirited Away"]


    # Let's test: Call a `print_all_ratings` function and pass it the `default_movie_list` as a parameter.
    print_all_ratings(default_movie_list)

    # We set up an infinite loop (`while True`) so that we can keep asking the
    # user the same question until they give us valid input ("1" or "2"). As
    # soon as a valid input is reached, the appropriate function runs and the
    # loop is terminated with "break".
    while True:

        # Enter search or ratings function.
        search_or_ratings = input("Would you like to search for a movie (1) or find the rating of a specific movie (2)?")

        if search_or_ratings == 1:
            # Ask user for movie title.
            movie_query = input("Enter the movie title: ")

            # If `search_or_ratings is 1`, call `list_search_results()`.
            list_search_results(movie_query)
            break
        elif search_or_ratings == 2:
            # Ask user for movie title.
            movie_query = input("Enter the movie title: ")

            # If `search_or_ratings` is 2, call `print_movie_rating()`.
            print_single_movie_rating(movie_query)
            break

        else:
            # If `search_or_ratings` is otherwise, give an error.
            print("Error: Your input must be 1 or 2!")


# This line tells Python to run `main()` when it first opens.
if __name__ == "__main__":
    main()
