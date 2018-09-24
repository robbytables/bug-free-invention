# Create a variable called search_or_ratings, set to "1".
# You should be able to change this between "1", "2", and "3" to change what your program prints.
search_or_ratings = 2

class Movie(object):
    """
    Movie objects contain all information about a particular movie,
    including the title and rating.
    """

    def __init__(self, movie_data):

        self.movie_data = movie_data
        # Store the raw data in this object so that we can use the
        # data in the getter functions.

    def get_movie_title(self):
        """
        get_movie_title is a getter function that returns the movie title.
        """

        # Return the title from the movie data.
        return self.movie_data["title"]

    def get_movie_rating(self):
        """
        get_movie_rating is a getter function that returns the rating.
        """

        # Return the rating from the movie data.
        return self.movie_data["rating"]

def return_single_movie_object(movie_title, movie_rating):
    """
    Take in the movie title and rating, and return the movie object.
    """

    return Movie({'title': movie_title, 'rating': movie_rating})

def list_search_results(movie_titles):
    """
    Print list of movies. Later, print a list of title results from a movie search.
    """
    
    # Loop through the list of titles and print them (indented with four spaces).
    for title in movie_titles:
        print("    " + title)

def print_single_movie_rating(movie_query):
    """
    Create a Movie object and print one movie's Rotten Tomatoes rating.
    """

    my_movie = return_single_movie_object(movie_query, 7)

    # Print the whole formatted string.
    print("The rating for", my_movie.get_movie_title(), "is",  my_movie.get_movie_rating())

def print_all_ratings(movie_list):
    """
    Take in a list of movies, create a movie object for each, and print the rating.
    """

    for movie in movie_list:
        movie_object = return_single_movie_object(movie, 4)
        print("The movie", movie_object.get_movie_title(), "has a rating of", movie_object.get_movie_rating())

# Create one main function that will call everything else.
def main():

    """
    Main is the entry point into the program, and it calls into the search or
    ratings functions depending on what the user decides to do.
    """

    # A hard-coded movie list with which to test.
    default_movie_list = ["Back to the Future", "Blade", "Spirited Away"]


    # Let's test: Call a print_all_ratings() function and pass it the default_movie_list as a parameter.
    print_all_ratings(default_movie_list)

    if search_or_ratings == 1:
        # If search_or_ratings is 1, call list_search_results().
        list_search_results(default_movie_list)
    elif search_or_ratings == 2:
        # If search_or_ratings is 2, call print_movie_rating().
        print_single_movie_rating("Moana")

    else:
        # If search_or_ratings is otherwise, give an error.
        print("Error: Your input must be 1 or 2!")


# This line tells Python to run main() when it first opens.
if __name__ == "__main__":
    main()
