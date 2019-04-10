# Example code for a page based system
import responder

# Create the API
api = responder.API()

# Define the route (include {data})
@api.route("/")
def index(req, resp):
    # Render template, passing data to Jinja2
    resp.content = api.template("home/index.html", user="what-ever")
    # No return values - response object is MUTABLE


api.run()
