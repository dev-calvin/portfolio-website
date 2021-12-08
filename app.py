import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    data = {
        'title' : 'Calvin McClure.',
        'home': {
            'a': 'I am a <span class=\'highlight\'>Software Engineer</span> specializing in software development, as well as network and system security. Recently I have been..',
            'b': 'Graduated from <span class=\'highlight\'>Arizona State University</span> <span class=\'text-muted\'>(2021)</span>',
            'c': 'Web and mobile app developer at <span class=\'highlight\'>XLR8 Development</span> <span class=\'text-muted\'>(2017-2021)</span>'
        },
        'aboutMe': '''Hi, I am Calvin and I have had an interest in tech my whole life. When I
                    was younger I never imagined I would learn so much about how it works. My
                    software education started in high school at the coding West-MEC program in
                    2015 where I got my intro to web development. After this I was sure it was
                    something I wanted to pursue professionally so I continued to Arizona State
                    University where I have now completed my Bachelors in Computer Science
                    (Cyber Security). I cannot wait to see where my degree and professional
                    experience will lead me to next. I am excited to learn new technologies and
                    spread into new roles!'''
    }
    return render_template('index.html', content=data)


@app.route('/hello')
def hello_world():
    target = os.environ.get('TARGET', 'World')
    return 'Hello {}!\n'.format(target)


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
