# movie-recommendation-tool
This Python script interacts with the OMDb API to fetch details about movies based on user input. It displays movie details such as title, year, rating, runtime, and plot summary, and provides recommendations based on IMDb ratings. The script saves fetched data to a JSON file and a SQLite database for easy access and storage of movie details.

How it Works:


1.The script prompts the user to enter the title of a movie.

2.It constructs a URL for the OMDb API using the movie title and an API key.

3.It makes a GET request to the OMDb API to fetch details about the specified movie.

4.The fetched data includes the movie's title, year of release, IMDb rating, runtime, and plot summary.

5.The script displays the movie details to the user, including the title, year, rating, runtime, and plot.

6.Based on the IMDb rating, the script provides recommendations on whether the movie is highly recommended, not recommended, or has an average rating.

7.It saves the movie details to a JSON file named movie_details.json using the json.dump() function.

8.It stores the movie details in a SQLite database named movies.db in a table named movies.

9.The script creates the database table if it doesn't exist and inserts the movie details into the table using SQL queries.

10.Finally, it prints a confirmation message indicating that the movie details have been saved to the database.
