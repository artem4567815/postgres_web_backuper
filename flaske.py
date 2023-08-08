from flask import Flask, render_template, request, redirect

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

from db import get_first_data
from config import conn_params

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///backupdata.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

passwords = [
    {
        "password_archive": "123",
        "key":"123",
        "host":"123",
        "port":"123",
        "user":"123",
        "password2":"123",
    }
]
data = get_first_data(conn_params, ["pg_catalog", "pg_toast", "information_schema"])
print(data)

@app.route('/')
def index():
    return render_template('index.html', data=data, passwords=passwords)


@app.route('/api/freq', methods=['post'])
def api_freq():
    for db in data:
        for shed in db["shed"]:
            ret = request.form.get(f"frequency_{db['db']}_{shed['sh']}")
            if ret == "daily":
                shed["freq"] = "Раз в день"
            elif ret == "weekly":
                shed["freq"] = "Раз в неделю"
            elif ret == "never":
                shed["freq"] = "Никогда"
    return redirect("/")


@app.route('/data', methods=['post'])
def data2():
    password_archive = request.form['password']
    key = request.form['key']
    host = request.form['login1']
    port = request.form['login2']
    user = request.form['login3']
    password = request.form['login4']
    passwords[0]["password_archive"] = password_archive
    passwords[0]["key"] = key
    passwords[0]["host"] = host
    passwords[0]["port"] = port
    passwords[0]["user"] = user
    passwords[0]["password2"] = password
    return redirect("/")

if __name__ == '__main__':
    app.run(port=8080, debug=True)