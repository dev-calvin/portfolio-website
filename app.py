import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    data = {
        'title' : 'Calvin McClure.'
    }
    return render_template('index.html', content=data)


@app.route('/hello')
def hello_world():
    target = os.environ.get('TARGET', 'World')
    return 'Hello {}!\n'.format(target)


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
