from api_instance import api

api.add_route("/static", static=True)


@api.route("/")
def index(_, resp):
    # Add relative path to the templates
    resp.content = api.template("home/index.html")
