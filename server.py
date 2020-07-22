from flask import Flask, render_template
import requests
import json
import database as db

app = Flask(__name__)

app.config['DEBUG'] = True


@app.route('/api/<github_username>')
def api(github_username):
    print("inside : api")
    db.DataBase.refresh(github_username)
    data = db.DataBase.get_data(github_username)
    if data is not None:
        data.sort(key=lambda x: int(x["stargazers_count"]),reverse=True)
        data = data[0:5]
        return render_template('index.html', data=data)
    return 'error'
