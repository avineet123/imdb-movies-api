## IMDB Movie API

An API interface to search and find movies by names, directors and genres and to manage imdb movie viewer/editor

It uses data from imdb.json

## Setting up project and initializing data
```
1. create a virtualenv 
2. virtualenv myenv
3. source myenv/bin/activate
4. pip install -r requirements.txt
5  ./manage.py migrate
6. ./manage.py runserver 7001
7. ./manage.py populate_movies
```


### API Request Examples

### Base API url
https://imdb-movie-api.herokuapp.com/api/movies

### Filter by name
https://imdb-movie-api.herokuapp.com/api/movies?name=wizard

### filter by movie name and director name
https://imdb-movie-api.herokuapp.com/api/movies?name=wizard&director=victor

### filter by genre name
https://imdb-movie-api.herokuapp.com/api/movies?genre=family
