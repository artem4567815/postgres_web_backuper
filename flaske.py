from flask import Flask, render_template

app = Flask(__name__)

# Sample data array
data = [
    {
        "db": "Database 1",
        "shed": [
            {"sh": "Collection 1", "freq": "Никогда"},
            {"sh": "Collection 2", "freq": "Раз в день"},
            {"sh": "Collection 3", "freq": "Раз в неделю"}
        ]
    },
    {
        "db": "Database 2",
        "shed": [
            {"sh": "Collection 4", "freq": "Раз в день"},
            {"sh": "Collection 5", "freq": "Никогда"},
            {"sh": "Collection 6", "freq": "Раз в неделю"}
        ]
    }
]

@app.route('/')
def index():
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(port=8080, debug=True)