import requests
import secret


valid_modes = ['ratings', 'search']

mode_prompt = 'Would you like to \'search\' or retrieve \'ratings\'?'
mode_reprompt = 'Please enter either \'search\' or \'ratings\'.'
movie_query_prompt = 'Enter a movie title:'


class OMDBException(Exception):
    """
    OMDBException represents an error returned by the OMDb API.
    """
    pass


class Movie():
    """
    `Movie` objects contain all information about a particular movie,
    including the title and rating.
    """

    def __init__(self, movie_data):
        self.title = movie_data['Title']
        self.ratings = movie_data['Ratings']
    
    def get_title(self):
        """
        `get_movie_title` is a getter function that returns the movie title.
        """
        return self.title

    def get_rating(self, source="Rotten Tomatoes"):
        """
        get_movie_rating is a getter function that returns the rating.
        """

        # There can be multiple ratings for each movie, so they are stored as a
        # list of ratings, each with a source and a rating. By default, we are
        # only interested in Rotten Tomatoes ratings, so we loop through each
        # rating and return it if the source is Rotten Tomatoes.
        for rating in self.ratings:
            if rating["Source"] == source:
                return rating["Value"]

        return "Rating for source {0} was not found!".format(source)

class OMDB(object):
    """
    OMDb objects represent clients to the OMDb API. It has helper methods for
    performing functions on the API.
    """
    movie_info_url = "http://www.omdbapi.com/?t={0}&apikey={1}"
    movie_search_url = "http://www.omdbapi.com/?s={0}&apikey={1}"

    def __init__(self, apikey):
        # Store the API key so it may be used later to build the authenticated URL.
        self.apikey = apikey

    def get_movie(self, movie_query):
        url = self.movie_info_url.format(movie_query, self.apikey)
        response_data = self.call_api(url)
        return Movie(response_data)
            
    def search_movies(self, movie_query):
        url = self.movie_search_url.format(movie_query, self.apikey)
        response_data = self.call_api(url)
        return response_data['Search']

    def call_api(self, url):
        response_data = requests.get(url).json()
        if "Error" in response_data:
            raise OMDBException(response_data['Error'])
        return response_data


def print_search_results(movie_query):
    omdb_client = OMDB(secret.AUTH_KEY)

    try:
        search_results = omdb_client.search_movies(movie_query)
    except OMDBException as error:
        print("OMDB Exception: {0}".format(error))
        return
    
    for index in range(len(search_results) - 1):
        print('{0}. {1}'.format(index, search_results[index]['Title']))

def print_movie_rating(movie_query):
    omdb_client = OMDB(secret.AUTH_KEY)

    try:
        movie = omdb_client.get_movie(movie_query)
    except OMDBException as error:
        print("OMDB Exception: {0}".format(error))
        return
    
    print("The rating for \"{0}\" is {1}.".format(movie.get_title(), movie.get_rating()))


    
def get_mode_from_user():
    mode = input(mode_prompt)
    while mode not in valid_modes:
        mode = input(mode_reprompt)
    return mode


def print_all_ratings(movie_list):
    """
    Take in a list of movies, create a `Movie` object for each, and print the rating.
    """
    for movie in movie_list:
        print_movie_rating(movie_query)

# Create one main function that will call everything else.
def main():

    """
    Main is the entry point into the program, and it calls into the search or
    ratings functions depending on what the user decides to do.
    """

    # Set the mode
    mode = get_mode_from_user()
    movie_query = input(movie_query_prompt)

    if mode == 'search':
        print_search_results(movie_query)
    elif mode == 'ratings':
        print_movie_rating(movie_query)
    else:
        print('Invalid mode')

# This line tells Python to run `main()` when it first opens.
if __name__ == "__main__":
    main()
