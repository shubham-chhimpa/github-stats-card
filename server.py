from flask import Flask, Response

import database as db

app = Flask(__name__)

app.config['DEBUG'] = True


@app.route('/api/<github_username>')
def api(github_username):
    print("inside : api")
    db.DataBase.refresh(github_username)
    data = db.DataBase.get_data(github_username)
    if data is not None:
        data.sort(key=lambda x: int(x["stargazers_count"]), reverse=True)
        svg = """
        <svg width="500" height="210" viewBox="0 0 500 210" fill="none" xmlns="http://www.w3.org/2000/svg">

    <rect
            x="0.5"
            y="0.5"
            width="500"
            height="99%"
            rx="4.5"
            fill="#FFFEFE"
            stroke="#E4E2E2"
    />

    <text x="100" y="20" style="fill:black;font-size:16">Shubham Chhimpa's Top Repos</text>
    <line x1="0" y1="40" x2="500" y2="40" style="stroke:rgb(255,0,0);stroke-width:1"/>

    <text x="20" y="60" style="fill:black;">Repo (📂)</text>
    <text x="300" y="60" style="fill:black;">Stars (⭐)</text>
    <text x="400" y="60" style="fill:black;">Forks (🍴)</text>
    <line x1="0" y1="70" x2="500" y2="70" style="stroke:rgb(255,0,0);stroke-width:1"/>

    <line x1="290" y1="40" x2="290" y2="190" style="stroke:rgb(255,0,0);stroke-width:1"/>
    <line x1="390" y1="40" x2="390" y2="190" style="stroke:rgb(255,0,0);stroke-width:1"/>

    <text x="20" y="90" style="fill:black;">""" + data[0]['name'] + """</text>
    <text x="300" y="90" style="fill:black;">""" + str(data[0]['stargazers_count']) + """</text>
    <text x="400" y="90" style="fill:black;">""" + str(data[0]['forks']) + """</text>
    <line x1="0" y1="100" x2="500" y2="100" style="stroke:rgb(255,0,0);stroke-width:1"/>

     <text x="20" y="120" style="fill:black;">""" + data[1]['name'] + """</text>
    <text x="300" y="120" style="fill:black;">""" + str(data[1]['stargazers_count']) + """</text>
    <text x="400" y="120" style="fill:black;">""" + str(data[1]['forks']) + """</text>
    <line x1="0" y1="130" x2="500" y2="130" style="stroke:rgb(255,0,0);stroke-width:1"/>

     <text x="20" y="150" style="fill:black;">""" + data[2]['name'] + """</text>
    <text x="300" y="150" style="fill:black;">""" + str(data[2]['stargazers_count']) + """</text>
    <text x="400" y="150" style="fill:black;">""" + str(data[2]['forks']) + """</text>
    <line x1="0" y1="160" x2="500" y2="160" style="stroke:rgb(255,0,0);stroke-width:1"/>

      <text x="20" y="180" style="fill:black;">""" + data[3]['name'] + """</text>
    <text x="300" y="180" style="fill:black;">""" + str(data[3]['stargazers_count']) + """</text>
    <text x="400" y="180" style="fill:black;">""" + str(data[3]['forks']) + """</text>
    <line x1="0" y1="190" x2="500" y2="190" style="stroke:rgb(255,0,0);stroke-width:1"/>

</svg>
        
              """

        return Response(
            svg,
            mimetype='image/svg+xml'
        )
    return 'error'
