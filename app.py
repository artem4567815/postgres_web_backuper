from flask import Flask, render_template, request, redirect
from flask_migrate import Migrate

from db import get_first_data
from config import conn_params
from model import db, Setings, Shedules

from model import *
import schedule
from backuper import Backuper
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///backupdata.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    passwords = Setings.query.all()
    pas = {}
    print(passwords)
    for p in passwords:
        print(p.value, p.name)
        pas[f"{p.name}"] = p.value
    print(pas)

    return render_template('index.html', data=get_data(), passwords=pas)


@app.route('/api/freq', methods=['post'])
def api_freq():
    for database in get_data():
        for shed in database["shed"]:
            ret = request.form.get(f"frequency_{database['db']}_{shed['sh']}")
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

def get_data():
    data = []
    with app.app_context():
        schedules = db.session.query(Shedules).all()

    for schedule in schedules:
        db_data = {'db': schedule.database, 'shed': []}
        db_data['shed'].append({'sh': schedule.schedule, 'freq': schedule.freq})
        data.append(db_data)

    return data


def doit():
    for database in data:
        for shed in database["shed"]:
            Backuper().create("test.zip", "postgres", shed['sh'], "12345678")


if __name__ == '__main__':

    data = get_first_data(conn_params, ["pg_catalog", "pg_toast", "information_schema"])

    with app.app_context():
        for i in data:
            for j in i["shed"]:
                existing_record = db.session.query(Shedules).filter_by(database=i["db"], schedule=j["sh"],
                                                                       freq="Никогда").first()
                if existing_record is None:
                    db.session.add(Shedules(database=i["db"], schedule=j["sh"]))
        db.session.commit()

    app.run(port=8080, debug=True, host="0.0.0.0")
