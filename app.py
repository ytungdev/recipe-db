from flask import Flask, request
from flask_cors import CORS, cross_origin

import os
from bson.json_util import dumps
from urllib import parse

import model.database as database
import model.models as models

app = Flask(__name__)
cors = CORS(app)
CORS(app)



db = database.Connection()



@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.get("/api")
def get_api():
    url = request.url
    param = dict(parse.parse_qsl(parse.urlsplit(url).query))
    print(url)
    print(param)
    return f'{param}'

@app.route("/test")
def testing():
    recipe = models.Recipe()
    recipe.example()
    res = db.save('recipes', recipe)
    print(res)
    show = db.list_collection('recipes')
    print(show)
    return []

@app.route("/recipes", methods=['GET'])
def recipes():
    res = db.list_collection('recipes')
    return res

@app.post("/recipe")
def post_recipe():
    # add new recipe
    res = db.list_collection('recipes')
    return res
    
@app.get("/recipe")
def get_recipe():
    # research recipe
    name = request.args.get('name', '')
    if name != '':
        res = db.findRecipe(name)
        return res
    return [name]



if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5001))
    app.run(debug=True, host='0.0.0.0', port=port)

