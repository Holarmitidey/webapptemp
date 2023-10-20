from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def fizzbuzz():
    numbers = list(range(1, 101))  # Create a list of numbers from 1 to 100
    return render_template('fizzbuzz.html', numbers=numbers)

if __name__ == '__main__':
    app.run()