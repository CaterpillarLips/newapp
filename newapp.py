from flask import Flask, render_template, request

app = Flask(__name__)
app.secret_key = "change-me-to-anything"

users = {
    "staff": generate_password_hash("bookworm"),
}

@app.route("/")
def shop():
    return "Would you like to buy a watermelon?"

@app.route("/flask")
def flask():
    books = ["Kind of Blue", "Rumours", "Thriller"]
    return render_template("flask.html", books=books)

@app.route("/bread")
def bread():
    return render_template("index.html", shop="Chapter & Verse")

@app.route("/search")
def search():
    query = request.args.get('q', '')
    books = []

    if query:
        all_albums = ["Abbey Road", "Dark Side of the Moon", "Thriller", "Back in Black"]
        albums = [a for a in all_albums if query.lower() in a.lower()]
    else:
        titles = ["How to win at chess", "Harry Potter", "Rich Dad Poor Dad"]
        authors = ["Levy Rozman", "J.K. Rowling", "Robert Kiyosaki"]
    new_id = max([b["id"] for b in books], default = 0) + 1
    books.append({"id": new_id, "titles": titles, "authors": authors})
    return render_template("search.html", query=query, books=books)

app.run(debug=True)

save_books()