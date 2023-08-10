from models import *
from flask import Flask, render_template, request, redirect
from flask_migrate import Migrate
from methods import *

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///backupdata.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

migrate = Migrate(app, db)


@app.route('/', methods=['get'])
def index():
    targets = get_schemas()
    records = create_records(targets)
    groups = get_groups(records)

    return render_template('index.html', groups=groups)


@app.route('/', methods=['post'])
def save():
    for database, schema in get_schemas():
        freq = request.form.get(f"frequency_{database}_{schema}")

        schema = Schema.query.filter_by(database=database, schema=schema).first()
        if schema and freq in ["daily", "weekly", "never"]:
            schema.freq = freq
    db.session.commit()

    return redirect("/")

if __name__ == '__main__':
    app.run(port=8080, debug=True, host="0.0.0.0")
