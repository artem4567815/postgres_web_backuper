from flask import Flask, render_template

app = Flask(__name__)

# Sample data array
data = [
    {
        "db": "api-med-bot",
        "shed": [
            {"sh": "erfdfv", "freq": "Никогда"},
            {"sh": "sdrse", "freq": "Раз в день"},
            {"sh": "pub", "freq": "Раз в неделю"}
        ]
    },
    {
        "db": "swed",
        "shed": [
            {"sh": "pub", "freq": "Раз в день"},
            {"sh": "sdf", "freq": "Никогда"},
            {"sh": "sdfsdf", "freq": "Раз в неделю"}
        ]
    }
]

@app.route('/')
def index():
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(port=8080, debug=True)