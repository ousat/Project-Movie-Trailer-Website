import webbrowser


class Movie:
	''' This class contains the title, storyline , poster image and youtube link of the movie.
	 	Also has a module to play the youtube trailer video.'''
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		self.title = movie_title  # the title of the movie
		self.storyline = movie_storyline  # the storyline of the movie
		self.poster_image_url = poster_image  # the poster image url directs to the poster image
		self.trailer_youtube_url = trailer_youtube  # youtube trailer video's url

	def show_trailer(self):
		# opens the youtube trailer in a web browser
		webbrowser.open(self.trailer_youtube_url)
