from flask import Flask, render_template, request, redirect

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

if __name__ == '__main__':
    app.run(port=8080, debug=True)