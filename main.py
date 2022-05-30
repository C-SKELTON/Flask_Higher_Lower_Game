from flask import Flask
import random

random_number = random.randint(0,9)
print(random_number)


app = Flask(__name__)

@app.route('/')
def home():
    return '<u><b><h1 style = "text-align: left">Guess a number between 0 and 9 </h1></b></u>' \
            '<img src ="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"</img>'

@app.route('/<int:guess>/')
def check_number(guess):
    if guess < random_number:
        return '<h1 style = "text-align: left; color:red"> Too low, try again!' \
               '<br>' \
               '<img src = "https://media.giphy.com/media/ZFFVNwIbjsKtP3lHYK/giphy.gif"</img>'
    if guess > random_number:
        return '<h1 style = "text-align: left; color:purple"> Too high, try again!' \
               '<br>' \
               '<img src = "https://media.giphy.com/media/3boPPdHk2ueo8/giphy.gif"</img>'

    if guess == random_number:
        return '<h1 style = "text-align: left; color:green"> You found me!' \
               '<br>' \
               '<img src = "https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"</img>'


if __name__== "__main__":
    app.run(debug=True)