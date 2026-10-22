from flask import Flask, render_template, request, session, redirect, flash, url_for
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "change-me-to-anything"

users = {
    "staff": generate_password_hash("bookworm"),
}

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        name = request.form["username"]
        pw = request.form["password"]
        if name in users and check_password_hash(users[name], pw):
            session["user"] = name
            return redirect(url_for("search"))
        flash("Wrong username or password")
    return render_template("login.html")

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
        all_titles = ["How to win at chess", "Harry Potter", "Rich Dad Poor Dad", "Testing testing"]
        all_authors = ["Levy Rozman", "J.K. Rowling", "Robert Kiyosaki"]
        books = [a for a in all_titles if query.lower() in a.lower()]
    else:
        titles = ["How to win at chess", "Harry Potter", "Rich Dad Poor Dad"]
        authors = ["Levy Rozman", "J.K. Rowling", "Robert Kiyosaki"]
    new_id = max([b["id"] for b in books], default = 0) + 1
    books.append({"id": new_id, "titles": titles, "authors": authors})
    return render_template("search.html", query=query, books=books)

app.run(debug=True)
