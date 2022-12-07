from flask import Flask, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return redirect('https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley')


app.run(host='0.0.0.0', port=81)
