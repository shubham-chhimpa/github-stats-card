from flask import Flask, render_template
import requests
import json
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)
app.config['DEBUG'] = True


@app.route('/<username>')
def api(username):
    # response = requests.get(f'https://api.github.com/users/{username}/repos')
    # if response.status_code == 200:
    #
    #     data = json.loads(response.text)
    #     print(data[0])
    #     return render_template('index.html', data=data)
    # else:
    #     return "error"
    data = [{
        "name": "Composi",
        "stargazers_count": 50,
        "forks": 30
    }]
    return render_template('index.html', data=data)
