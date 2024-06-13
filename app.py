from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Home Page"


@app.route("/about/")
def about():
    return "About Page"

def bedrooms():
    return "Bedrooms Page"
app.add_url_rule("/bedrooms", view_func=bedrooms)


@app.route("/admin")
def admin_page():
    return "Here is Admin Page"


if __name__ == "__main__":
    app.run(host="localhost",port=4500,debug=True )