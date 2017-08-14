import webbrowser

#Module that defines storage classes for Movie trailer website
#Parent class Video defines a generic storage container for video objects
#Class Movie, subclass of Video defines a more specific storage container for Movie objects

#Class Video to represent a generic video object
class Video():
    """
    This class represents a Video object.

    Attributes:
        video_title: Title of the video
        video_duration: Total duration of the video in minutes
        video_year: When this video was released
    """

    #Constructor
    def __init__(self, title, duration, year ):
        #initialize video_title, video_duration and video_year instance attributes
        self.video_title = title
        self.video_duration = duration
        self.video_year = year

#Class Movie - subclass of Video that also holds additional movie specific information
class Movie(Video):
    """
    This class represents a Movie object. It is being inherited from class Video.
    As such, it inherits attributes video_title and video_duration from its parent
    class.

    Attributes:
        video_title: Title of the movie (inherited)
        video_duration: Duration of the movie (inherited)
        video_year: Year when the movie was released (inherited)
        movie_storyline: Main plot of the movie
        movie_poster_url: URL to the movie poster image
        movie_trailer_url: URL to the moie trailer on YouTube

    Behavior:
        show_trailer(): Launches the YouTube trailer link

    """
    #Constructor
    #Initializes a Movie instance using the supplied parameters
    def __init__(self, title, duration, year, storyline,
                 poster_url, trailer_url):
        #Call the parent constructor to populate video_title, video_duration and
        #video_year
        Video.__init__(self, title, duration, year)
        #initialize movie_storyline, movie_poster_url and movie_trailer_url instance attributes
        self.movie_storyline = storyline
        self.movie_poster_url = poster_url
        self.movie_trailer_url = trailer_url

    #Launches the YouTube video URL pointed by the trailer_url attribute
    #in the default browser
    def show_trailer(self):
        webbrowser.open(self.movie_trailer_url)
