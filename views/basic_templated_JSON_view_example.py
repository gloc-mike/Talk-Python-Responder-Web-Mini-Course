# Example code for a JSON based view
import responder

from data import db

# Create the API
api = responder.API()

# Define the route (include {data})
@api.route("/api/movies/search/{keyword}")
def search(req, resp, keyword: str):
    # search the database using the supplied keyword
    movies = db.search_keyword(keyword)

    # set the media property to indicate JSON
    resp.media = {
        "keyword": keyword,
        "result": movies
    }
    # pass the return data (keyword & result, etc.) as dicts/JSON serializable


api.run()
