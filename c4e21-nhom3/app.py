from flask import Flask, render_template, request, redirect, url_for
from models import mlab
from models.food import Food
mlab.connect()
app = Flask(__name__)

@app.route("/home")
def home():
    # all_home = home.objects()
    # return render_template("home.html", home=all_home)
    return render_template("home.html")
@app.route("/new")
def new():
    foods = Food.objects(chu_de = "couple")
    return render_template("new.html", foods = foods)


@app.route("/new1/<food_id>")
def new1(food_id):
    food = Food.objects().with_id(food_id)
    return render_template("new1.html", food = food)
if __name__ == "__main__":
    app.run(debug=True)