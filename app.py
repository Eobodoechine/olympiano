import os
from flask import (
    Flask,
    render_template,
    request)

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/Overview.html')
def overview():
    return render_template("Overview.html")


@app.route('/AboutUs.html')
def about_us():
    return render_template("AboutUs.html")


@app.route('/DataViz.html')
def data_viz():
    return render_template("DataViz.html")


@app.route('/GraphA.html')
def graph_a():
    return render_template("GraphA.html")


@app.route('/GraphB.html')
def graph_b():
    return render_template("GraphB.html")


@app.route('/GraphC.html')
def graph_c():
    return render_template("GraphC.html")

@app.route('/GraphD.html')
def graph_d():
    return render_template("GraphD.html")

@app.route('/GraphE.html')
def graph_e():
    return render_template("GraphE.html")

@app.route('/GraphF.html')
def graph_f():
    return render_template("GraphF.html")


if __name__ == '__main__':
    app.run(debug=True)
