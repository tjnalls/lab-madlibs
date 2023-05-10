"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    "awesome",
    "terrific",
    "fantastic",
    "neato",
    "fantabulous",
    "wowza",
    "oh-so-not-meh",
    "brilliant",
    "ducky",
    "coolio",
    "incredible",
    "wonderful",
    "smashing",
    "lovely",
]


@app.route("/")
def start_here():
    """Display homepage."""

    return render_template("hello.html")


@app.route("/hello")
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route("/greet")
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html", person=player, compliment=compliment)

@app.route("/game")
def game_choice():
    player_choice = request.args.get("game")
    if player_choice == "yes":
        return render_template ("game.html")
    if player_choice == "no":
        return render_template ("goodbye.html")


@app.route("/madlib")
def madlib_fun():
    color_input = request.args.get("color")
    noun_input = request.args.get("noun")
    people_input = request.args.get("people")
    adj_input = request.args.get("adjective")

    return render_template("madlib.html", color=color_input, noun=noun_input,people=people_input, adjective=adj_input)

    

@app.route("/goodbye")
def end_here():
    """Display goodbye page."""

    return render_template("goodbye.html")

if __name__ == "__main__":
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, port=3000, host="0.0.0.0")
