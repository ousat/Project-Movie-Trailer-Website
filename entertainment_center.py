import media
import fresh_tomatoes
import youtube_search
import tmdbsimple as tmdb
# tmdb api key to fetch movie details
tmdb.API_KEY = '99df58ea428a24bd08801335c2c35789'
# list of movies whose details will be fetched and saved
movie_names = ['Kong: Skull Island',
               'Avengers: Infinity War',
               'Star Wars: The Last Jedi',
               'Justice League',
               'Wreck-It Ralph',
               'Ready Player One',
               'The Shape of Water',
               'Jumanji: Welcome to the Jungle',
               'Pacific Rim']
# initializing empty movies list to save all Movie objects
movies = []
# looping through the saved titles
for movie_title in movie_names:
    # initializing tmdb object
    search = tmdb.Search()
    # querying tmdb object to search for the movie title
    response = search.movie(query=movie_title)
    # looping through search results
    for s in search.results:
        # check if the result title is the same as movie title
        if s['title'] == movie_title:
            # saves the movie poster path
            poster_path = "https://image.tmdb.org/t/p/w500" + s['poster_path']
            search_query = movie_title + " trailer"
            # gets youtube trailer video's url
            youtube_trailer_url = youtube_search.search(search_query)
            # creating a local movie object with title, plot , poster image
            # and youtube trailer video
            movie_object = media.Movie(s['title'],
                                       s['overview'],
                                       poster_path,
                                       youtube_trailer_url)
            # adding the movie object to movies lists
            movies.append(movie_object)
            # breaking loop after appropriate result object
            # to avoid looping through extra results
            break

# calling the open_movies_page function from fresh tomatoes
# passing the list of all the movie objects as a parameter
fresh_tomatoes.open_movies_page(movies)
