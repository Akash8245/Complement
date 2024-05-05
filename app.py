from flask import Flask,render_template
from flask_restful import Resource,Api
from compliment import Compliment as comp_method

app = Flask(__name__)
api = Api(app)


class Compliment(Resource):
    def get(self):
        return {"compliment" : comp_method().make_compliment()}

api.add_resource(Compliment,"/compliment")

@app.route("/")
def index():
    return render_template("index.html")

