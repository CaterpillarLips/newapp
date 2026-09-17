from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def shop():
    return "Would you like to buy a watermelon?"

@app.route("/flask")
def flask():
    albums = ["Kind of Blue", "Rumours", "Thriller"]
    return render_template("flask.html", albums=albums)

@app.route("/bread")
def bread():
    return render_template("index.html", shop="Chapter & Verse")

@app.route("/search")
def search():
    query = request.args.get('q', '')
    albums = []

    if query:
        all_albums = ["Abbey Road", "Dark Side of the Moon", "Thriller", "Back in Black"]
        albums = [a for a in all_albums if query.lower() in a.lower()]
    else:
        albums = ["Abbey Road", "Dark Side of the Moon", "Thriller"]

    return render_template("search.html", query=query, albums=albums)

app.run(debug=True)