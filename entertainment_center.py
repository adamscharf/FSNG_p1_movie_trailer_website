import media
import fresh_tomatoes

# Create instances of Movie
lion_king = media.Movie("The Lion King",
                        "https://upload.wikimedia.org/wikipedia/en/3/3d/The_Lion_King_poster.jpg",
                        "https://www.youtube.com/watch?v=GaJWzJfoXlE",
                        "1994")

frequency = media.Movie("Frequency",
                        "https://upload.wikimedia.org/wikipedia/en/7/7f/Frequency_film.jpg",
                        "https://www.youtube.com/watch?v=i6VQxn6HK_c",
                        "2000")

big_hero_6 = media.Movie("Big Hero 6",
                         "https://upload.wikimedia.org/wikipedia/en/4/4b/Big_Hero_6_%28film%29_poster.jpg",
                         "https://www.youtube.com/watch?v=z3biFxZIJOQ",
                         "2014")

intestellar = media.Movie("Interstellar",
                          "http://t1.gstatic.com/images?q=tbn:ANd9GcRf61mker2o4KH3CbVE7Zw5B1-VogMH8LfZHEaq3UdCMLxARZAB",
                          "https://www.youtube.com/watch?v=2LqzF5WauAw",
                          "2014")

# Add favorite movies to list
movies = [lion_king, frequency, big_hero_6, intestellar]

# Call function that runs the program
fresh_tomatoes.open_movies_page(movies)
