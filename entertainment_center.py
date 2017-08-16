import media
import fresh_tomatoes

#
# Create Movie instances
#   - Title
#   - Movie duration in minutes
#   - Year released
#   - Movie synopsis
#   - Movie poster url
#   - Movie YouTube trailer url
#

# 1. O Brother, Where Art Thou?
oh_brother = media.Movie("O Brother, Where Art Thou?",
                         108,
                         2000,
                         "In the Depression-era deep South, three escapees"
                         " from a Mississippi prison chain gang: Everett"
                         " Ulysses McGill, sweet and simple Delmar, and the"
                         " perpetually angry Pete, embark on the adventure"
                         " of a lifetime as they set out to pursue their"
                         " freedom and return to their homes.",
                         "https://resizing.flixster.com/eTgb1y_a5-FDH78lZRemqkAimPU=/206x305/v1.bTsxMTIwODQwNztqOzE3NDk5OzEyMDA7MTIwMDsxNjAw",  # NOQA
                         "https://www.youtube.com/watch?v=eW9Xo2HtlJI")


# 2. Big Lebowski
big_lebowski = media.Movie("The Big Lebowski",
                           109,
                           1998,
                           "The plot of this Raymond Chandler-esque comedy"
                           " crime caper from the Coen Brothers (Joel Coen and"
                           " Ethan Coen) pivots around a case of mistaken"
                           " identity complicated by extortion,"
                           " double-crosses, deception, embezzlement, sex,"
                           " pot, and gallons of White Russians"
                           " (made with fresh cream, please). In 1991,"
                           " unemployed '60s refugee Jeff The Dude Lebowski"
                           " (Jeff Bridges) grooves into his laid-back Los"
                           " Angeles lifestyle. One of the laziest men in LA,"
                           " he enjoys hanging with his bowling buddies,"
                           " pompous security-store owner Walter Sobchak"
                           " (John Goodman) and mild-mannered ex-surfer Donny"
                           " (Steve Buscemi). However, the Dude's life takes"
                           " an alternate route the afternoon two goons break"
                           " into his threadbare Venice, California, bungalow,"
                           " rough him up, and urinate on his rug.",
                           "http://img.moviepostershop.com/the-big-lebowski-movie-poster-1998-1010475636.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=cd-go0oBF4Y")

# 3. Pulp Fiction
pulp_fiction = media.Movie("Pulp Fiction",
                           178,
                           1994,
                           "Outrageously violent, time-twisting, and in love"
                           " with language, Pulp Fiction was widely considered"
                           " the most influential American movie of the 1990s."
                           " Director and co-screenwriter Quentin Tarantino"
                           " synthesized such seemingly disparate traditions"
                           " as the syncopated language of David Mamet; the"
                           " serious violence of American gangster movies,"
                           " crime movies, and films noirs mixed up with the"
                           " wacky violence of cartoons, video games, and"
                           " Japanese animation",
                           "https://resizing.flixster.com/D0f_tH49v1BCOQVjW2VWcdakk2c=/206x305/v1.bTsxMTE3NjEwNTtqOzE3NDk5OzEyMDA7ODAwOzEyMDA",  # NOQA
                           "https://www.youtube.com/watch?v=s7EdQ4FqbhY")

# 4. The Transporter
transporter = media.Movie("The Transporter",
                          92,
                          2002,
                          "An outlaw finds his life becoming all the more"
                          " dangerous when he turns against a gang of"
                          " criminals in this action drama. Frank Martin"
                          " (Jason Statham) is a former Special Forces"
                          " officer who lives on the French Mediterranean"
                          " and has a lucrative second career as a underworld"
                          " courier for hire. Martin will deliver anything"
                          " anywhere, but he has three iron-clad rules"
                          " -once the plan is in motion it cannot be changed",
                          "https://images-na.ssl-images-amazon.com/images/M/MV5BMTk2NDc2MDAxN15BMl5BanBnXkFtZTYwNDc1NDY2._V1_UY268_CR2,0,182,268_AL_.jpg",  # NOQA
                          "https://www.youtube.com/watch?v=0poXFSvX0_4")

# 5. The Dark Knight
dark_knight = media.Movie("The Dark Knight",
                          152,
                          2008,
                          "Christopher Nolan steps back into the director's"
                          " chair for this sequel to Batman Begins, which"
                          " finds the titular superhero coming face to face"
                          " with his greatest nemesis -- the dreaded Joker."
                          " Christian Bale returns to the role of Batman,"
                          " Maggie Gyllenhaal takes over the role of Rachel"
                          " Dawes (played by Katie Holmes in Batman Begins),"
                          " and Brokeback Mountain star Heath Ledger dons the"
                          " ghoulishly gleeful Joker",
                          "https://resizing.flixster.com/bv_cmSXJnLDWb0mRvZ9dXs9Tkeo=/206x305/v1.bTsxMTE2NTE2MDtqOzE3NDk5OzEyMDA7ODAwOzEyMDA",  # NOQA
                          "https://www.youtube.com/watch?v=qY3UkAHufLY")

# 6 Interstellar
interstellar = media.Movie("Interstellar",
                           169,
                           2014,
                           "With our time on Earth coming to an end, a team of"
                           " explorers undertakes the most important mission"
                           " in human history; traveling beyond this galaxy"
                           " to discover whether mankind has a future among"
                           " the stars.",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BMjIxNTU4MzY4MF5BMl5BanBnXkFtZTgwMzM4ODI3MjE@._V1_SY1000_CR0,0,640,1000_AL_.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=zSWdZVtXT7E")

# Now create a list of all these Movie objects
movies = [oh_brother,
          big_lebowski,
          pulp_fiction,
          transporter,
          dark_knight,
          interstellar]

# Call the fresh_tomatoes' open_movies_page function
fresh_tomatoes.open_movies_page(movies)
