import os

"""
- Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie, and 'q' to quit:

- Add movies
- See movies
- Find a movie
- Stop running the program

Tasks:
[x]: Decide where to store a movies
[x]: What is the format of a movie?
[x]: Show the user the main interface and get their input
[x]: Allow users to add movies
[x]: Show all their movies
[x]: Find a movie
[x]: Stop running the program when they type 'q'
"""

movies = []


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def add_movies():
    clear()
    message = "Enter the name, the director and the year of release of the movie: (name, director, year) "
    print('-' * len(message))
    movies_input = input(message).split(',')
    movies.append({'name': movies_input[0], 'director': movies_input[1], 'year': int(movies_input[2])})
    print()


def show_movies():
    clear()
    for movie in movies:
        show_movies_details(movie)


def show_movies_details(movie):
    message = f"The title : {movie['name']}, Directed by: {movie['director']}, In the {movie['year']}"
    print('-' * len(message))
    print(message)
    print('')


def find_movie():
    clear()
    search_input = input("Enter the Title or the Director of the movie you are searching for : ").lower()
    for movie in movies:
        if movie['name'].lower() == search_input or movie['director'].lower() == search_input:
            print("Here's your movie")
            print(f"The title : {movie['name']}, Directed by: {movie['director']}, In the {movie['year']}")
        else:
            print("Not found")


def menu():
    clear()
    while True:

        user_input = input("Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie, and 'q' to quit: ")

        if user_input == 'a':
            add_movies()

        elif user_input == 'l':
            show_movies()

        elif user_input == 'f':
            find_movie()

        elif user_input == 'q':
            print("Stopping program...")
            break
        else:
            print("Unknown command-please try again. ")


menu()
