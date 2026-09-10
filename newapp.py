from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    #return "This is a watermelon shop"
    return render_template("index.html")

@app.route("/shop")
def about():
    return "Would you like to buy a watermelon?"

app.run(debug=True)