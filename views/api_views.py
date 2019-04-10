import responder

from api_instance import api
from data import db

RESPONSE_COUNT_MAX = 10

# Because this is a ASGI framework based on Starlette
# we could use "async" and "await" if the DB supports ASync behaviour (which it
# does NOT in in this play program) -- see position of ""async" & "await"
# @api.route("/api/search/{keyword}")
# async def search_by_keyword(_, resp: responder.Response, keyword: str):
#     movies = await db.search_keyword(keyword)
#     print(f"Searching for movies by keyword: {keyword}")
#
#     limited = len(movies) > RESPONSE_COUNT_MAX
#     if limited:
#         movies = movies[:10]
#
#     movie_dicts = [
#         db.movie_to_dict(m)
#         for m in movies
#     ]
#
#     resp.media = {"keyword": keyword, "hits": movie_dicts, "truncated_results": limited}


# Search movies
# GET /api/search/{keyword}
@api.route("/api/search/{keyword}")
def search_by_keyword(_, resp: responder.Response, keyword: str):
    movies = db.search_keyword(keyword)
    print(f"Searching for movies by keyword: {keyword}")

    limited = len(movies) > RESPONSE_COUNT_MAX
    if limited:
        movies = movies[:10]

    movie_dicts = [
        db.movie_to_dict(m)
        for m in movies
    ]

    resp.media = {"keyword": keyword, "hits": movie_dicts, "truncated_results": limited}


# Movies by director
# GET /api/director/{director_name}
@api.route("/api/director/{director_name}")
def search_by_director(_, resp: responder.Response, director_name: str):
    movies = db.search_director(director_name)
    print(f"Searching for movies by director_name: {director_name}")

    limited = len(movies) > RESPONSE_COUNT_MAX
    if limited:
        movies = movies[:10]

    movie_dicts = [
        db.movie_to_dict(m)
        for m in movies
    ]

    resp.media = {"keyword": director_name, "hits": movie_dicts, "truncated_results": limited}


# Movie by IMDB code
# GET /api/movie/{imdb_number}
@api.route("/api/movie/{imdb_number}")
def movie_by_imdb(_, resp: responder.Response, imdb_number: str):
    print(f"Searching for movies by imdb_number: {imdb_number}")
    movie = db.find_by_imdb(imdb_number)
    resp.media = db.movie_to_dict(movie)

# Top 10 Movies (by IMDB score)
# GET /api/movie/top

# All genres
# GET /api/movie/genre/all

# Top movies for a given genres
# GET /api/movie/genre/{genre}
