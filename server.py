from flask import Flask, render_template
import requests
import json
import database as db

app = Flask(__name__)

app.config['DEBUG'] = True


@app.route('/api/<github_username>')
def api(github_username):
    db.DataBase.refresh(github_username)
    data = db.DataBase.get_data(github_username)
    print("inside : api")
    if data is not None:
        return render_template('index.html', data=data)
    return 'error'
