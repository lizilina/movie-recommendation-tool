import requests
import json
import sqlite3

api_key = '690d1758'
title = input("Enter the title of the movie: ")

url = f"http://www.omdbapi.com/?t={title}&apikey={'690d1758'}"
response = requests.get(url)

# Using functions/attributes of the requests module
print(f'URL: {response.url}')
print(f'Status Code: {response.status_code}')
print(f'Response headers: {response.headers}')

# Gives user the details about the move.
if response.status_code == 200:
    movie_details = response.json()

    title = movie_details['Title']
    year = movie_details['Year']
    rating = movie_details['imdbRating']
    runtime = movie_details['Runtime']
    plot = movie_details['Plot']

    print(f"Title: {title}")
    print(f"Year: {year}")
    print(f"Rating: {rating}")
    print(f"Length: {runtime}")
    print(f"Description: {plot}")


# Gives recommendations based on the rating
    try:
        Rating = float(rating)
        if Rating >= 8.0:
            print("This movie is highly recommended!")
        elif Rating < 5.0:
            print("I do not recommend watching this movie.")
        else:
            print("The movie has an avarage rating.")
    except ValueError:
        print("Information is not available.")

    # Save movie details to a file
    with open('movie_details.json', 'w') as json_file:
        json.dump(movie_details, json_file, indent=4)
    print("Data saved to movie_details.json")

# # Save movie details to a SQLite database
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS movies (title TEXT, year TEXT, rating TEXT, runtime TEXT,plot TEXT)''')
    cursor.execute('''INSERT INTO movies (title, year, rating, runtime, plot)VALUES (?, ?, ?, ?, ?)''',(title, year, rating, runtime, plot))

    conn.commit()
    conn.close()
    print("Movie details saved to database.")
else:
    print("Movie not found :(")
