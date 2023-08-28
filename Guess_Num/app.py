from flask import Flask, render_template, request
from random import randint

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")



@app.route('/game', methods=['POST'])
def start_game():
    range_value = request.form['range']
    return render_template('guess.html', range_value=range_value)



@app.route('/guess', methods=['GET','POST'])
def check_guess():
    range_value = int(request.form['range_value'])
    target_number = randint(1, range_value)
    user_guess = int(request.form['guess'])
    feedback = ""

    if user_guess < target_number:
        feedback = "Guessed too low!"
    elif user_guess > target_number:
        feedback = "Guessed too high!"
    else:
        feedback = "Congratulations! You guessed correctly."

    return render_template('guess.html', range_value=range_value, target_number=target_number, feedback=feedback)
  


if __name__=="__main__":
  app.run(host='0.0.0.0',debug=True)