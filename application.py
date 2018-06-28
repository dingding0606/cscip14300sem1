from flask import Flask, render_template, request

app = Flask(__name__)  # let flask know where to find files

users = []

# a list of dicts that shows the status of each day
days = [1, 2, 3, 4, 5, 6, 7]

notes = [
        {
            'title': 'HTTP notes',
            'url':'httpnotes',
            'index': 1,
            'author': 'Steven Wu',
            'content': "test1, foo, foo."
        },
        {
            'title': 'HTML notes',
            'url':'htmlnotes',
            'index': 1,
            'author': 'Steven Wu',
            'content': "test2, 2, 2, sad, asdf, asd."
        },
        {
            'title': 'Python notes',
            'url':'pythonnotes',
            'index': 2,
            'author': 'Steven Wu',
            'content': "asdfljk,das,a.f jasdfasdf,."
        }
]

app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/")  # flask decorator: add additional functionalities to function below
@app.route("/home")  # add both route for one functionality
def home():
    return render_template("home.html", days=days, notes=notes)

@app.route("/register", methods=["POST"])
def register():
    username = request.form.get("username")
    password = request.form.get("password")
    if not username or not password:
        return render_template("noaccess.html")
    users.append({username, password})
    return render_template("success.html")

@app.route("/noaccess")
def noaccess():
    return render_template("noaccess.html")

@app.route("/httpnotes")
def httpnotes():
    return render_template("httpnotes.html", content=notes[0]['content'])

@app.route("/htmlnotes")
def htmlnotes():
    return render_template("htmlnotes.html", content=notes[1]['content'])

@app.route("/pythonnotes")
def pythonnotes():
    return render_template("pythonnotes.html", content=notes[2]['content'])
