# Shamelessly copied from http://flask.pocoo.org/docs/quickstart/

from flask import Flask, render_template

@app.route('/')
def index():
    return render_template('index.html')
    
if __name__ == '__main__':
    app.run()

app = Flask(__name__)

