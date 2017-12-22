import media
import fresh_tomatoes

# creating instance of movie class for avengers infinity war
infinity_war = media.Movie("Avengers : Infinity War",
			   "The Avengers and their allies must be willing to sacrifice all in an attempt to defeat the powerful Thanos before his blitz of devastation and ruin puts an end to the universe.",
			   "https://upload.wikimedia.org/wikipedia/en/9/90/Avengers_Infinity_War.jpg",
			   "https://www.youtube.com/watch?v=6ZfuNTqbHE8")

# creating instance of movie class for star wars last jedi
the_last_jedi = media.Movie("Star Wars : The Last Jedi",
						   "Rey develops her newly discovered abilities with the guidance of Luke Skywalker, who is unsettled by the strength of her powers. Meanwhile, the Resistance prepares to do battle with the First Order.",
						   "https://upload.wikimedia.org/wikipedia/en/7/7f/Star_Wars_The_Last_Jedi.jpg",
						   "https://www.youtube.com/watch?v=Q0CbN8sfihY")

# creating instance of movie class for justice league
justice_league = media.Movie("Justice League",
							 "Fueled by his restored faith in humanity and inspired by Superman's selfless act, Bruce Wayne enlists the help of his newfound ally, Diana Prince, to face an even greater enemy.",
							 "https://upload.wikimedia.org/wikipedia/en/3/31/Justice_League_film_poster.jpg",
							 "https://www.youtube.com/watch?v=r9-DM9uBtVI")

# creating instance of movie class for wreck it ralph
wreck_it_ralph = media.Movie("Wreck it! Raplh!",
							 "A video game villain wants to be a hero and sets out to fulfill his dream, but his quest brings havoc to the whole arcade where he lives.",
							 "https://upload.wikimedia.org/wikipedia/en/1/15/Wreckitralphposter.jpeg",
							 "https://www.youtube.com/watch?v=87E6N7ToCxs")

# creating instance of movie class for ready player one
ready_player_one = media.Movie("Ready Player One",
							 "When the creator of a virtual reality world called the OASIS dies, he releases a video in which he challenges all OASIS users to find his Easter Egg, which will give the finder his fortune. Wade Watts finds the first clue and starts a race for the Egg.",
							 "https://upload.wikimedia.org/wikipedia/en/7/74/Ready_Player_One_%28film%29.png",
							 "https://www.youtube.com/watch?v=4aifnWlP_sM")

# creating instance of movie class for shape of water
shape_of_water = media.Movie("The Shape of Water",
							 "In a 1960s research facility, a mute janitor forms a relationship with an aquatic creature.",
							 "https://upload.wikimedia.org/wikipedia/en/3/37/The_Shape_of_Water_%28film%29.png",
							 "https://www.youtube.com/watch?v=XFYWazblaUA")

# creating instance of movie class for dunkirk
dunkirk = media.Movie("Dunkirk",
					  "Allied soldiers from Belgium, the British Empire and France are surrounded by the German Army, and evacuated during a fierce battle in World War II.",
					  "https://upload.wikimedia.org/wikipedia/en/1/15/Dunkirk_Film_poster.jpg",
					  "https://www.youtube.com/watch?v=XRtZUkAR2u4")

# creating instance of movie class for jumanji welcome to the jungle
jumanji_welcome_to_the_jungle = media.Movie("Jumanji Welcome to the Jungle",
							 			    "Four teenagers discover an old video game console and are literally drawn into the game's jungle setting becoming the adult avatars they chose.",
							 				"https://upload.wikimedia.org/wikipedia/en/d/dc/Jumanji_Welcome_to_the_Jungle.png",
							 				"https://www.youtube.com/watch?v=2QKg5SZ_35I")

# creating instance of movie class for pacific rim uprising
pacific_rim_uprising = media.Movie("Pacific Rim - Uprising",
							 "Jake Pentecost, son of Stacker Pentecost, reunites with Mako Mori to lead a new generation of Jaeger pilots, including rival Lambert and 15-year-old hacker Amara, against a new Kaiju threat.",
							 "https://upload.wikimedia.org/wikipedia/en/2/2e/Pacificrim2-poster.jpg",
							 "https://www.youtube.com/watch?v=_EhiLLOhVis")

# a list of all the movie objects initialized assigned to movies
movies = [infinity_war, the_last_jedi, justice_league, ready_player_one, wreck_it_ralph, shape_of_water, dunkirk, jumanji_welcome_to_the_jungle, pacific_rim_uprising]

# calling the open_movies_page function from fresh tomatoes passing the list of all the movie objects as a parameter
fresh_tomatoes.open_movies_page(movies)
