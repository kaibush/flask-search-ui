import datetime

from flask import Flask, render_template, request
from models.form import SearchForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "12345678"


@app.route("/")
def hello_world():
    form = SearchForm()
    return render_template("spatial/index.html", form=form)


@app.route("/search_creater")
def search_creater():
    form = SearchForm()
    search = request.args.get("query", "") + str(datetime.datetime.now())
    return render_template("result_search.html", form=form, search=search)


if __name__ == "__main__":
    app.run()
