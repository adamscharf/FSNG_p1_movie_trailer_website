class Movie():
    """A class used to represent my favorite movies.

    Longer class information....
    Longer class information....

    Attributes:
        title: Title of the movie
        poster_image_url: URL to the poster image of the movie
        trailer_youtube_url: URL to the trailer on youtube
        year = Release year
    """

    def __init__(self, title, poster_image_url, trailer_youtube_url, year):
        """Inits Movie with all attributes"""
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.year = year
