from flask import Flask, render_template, request
import requests, json
app = Flask(__name__)

url = "https://openlibrary.org/search.json?q=dracula/&scrlybrkr=159d0152"
response = requests.get(url, verify = False)
data = response.json()

with open("data.json") as f:
    data = response.json()

print(data)
albums = data["results"]      # the list of albums

books = data["docs"]
for book in books:
    print (book["title"]) # prints each title

app.run(debug=True)

books = [{"title": "Dracula", "author": "Stoker"}]
print(json.dumps(books))
[{"title"}]
#try:
    #with open("books.json", "r") as f:
        #books = json.load(f)

def save_books():
    with open("books.json", "w") as f:
        json.dump(books, f)

@app.route("/")
def shop():
    #return "Would you like to buy a watermelon?"
    return data
    #return render_template(
        #"shop.html", albums=albums)


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
        all_albums = ["123", '!#"', "Abbey Road", "Dark Side of the Moon", "Thriller", "Back in Black"]
        albums = [i for i in all_albums if query.lower() in i.lower()]
    else:
        albums = ["Abbey Road", "Dark Side of the Moon", "Thriller"]

    return render_template("search.html", query=query, albums=albums)

app.run(debug=True)

save_books()