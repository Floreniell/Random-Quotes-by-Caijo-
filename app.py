from flask import Flask, render_template
import random

app = Flask(__name__)

# List of 50 random quotes
quotes = [
    "The best way to predict the future is to invent it.",
    "Life is 10% what happens to us and 90% how we react to it.",
    "In the end, we will remember not the words of our enemies, but the silence of our friends.",
    # Add more quotes as needed
    "Do not take life too seriously. You will never get out of it alive.",
    "You only live once, but if you do it right, once is enough."
]

@app.route('/')
def index():
    # Pick a random quote
    quote = random.choice(quotes)
    return render_template('index.html', quote=quote)

@app.route('/next')
def next_quote():
    # Pick another random quote
    quote = random.choice(quotes)
    return render_template('index.html', quote=quote)

if __name__ == '__main__':
    app.run(debug=True)
