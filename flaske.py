from flask import Flask, render_template

app = Flask(__name__)

# Sample data array
data = [
    {
        "db": "Database 1",
        "shed": [
            {"sh": "Collection 1", "freq": "Never"},
            {"sh": "Collection 2", "freq": "Once a day"},
            {"sh": "Collection 3", "freq": "Once a week"}
        ]
    },
    {
        "db": "Database 2",
        "shed": [
            {"sh": "Collection 4", "freq": "Once a day"},
            {"sh": "Collection 5", "freq": "Never"},
            {"sh": "Collection 6", "freq": "Once a week"}
        ]
    }
]

@app.route('/')
def index():
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run()