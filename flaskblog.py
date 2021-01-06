from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        "author": "Jan Kowalski",
        "title": "Blog post 1",
        "content": "First post content",
        "date_posted": "1 stycznia 2021"
    },
    {
        "author": "Maria Kowalska",
        "title": "Blog post 2",
        "content": "Seconds post content",
        "date_posted": "4 stycznia 2021"
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html", title="About")

if __name__ == "__main__":
    app.run(debug=True)