from flask import Flask, redirect, render_template
app = Flask(__name__, static_folder='style')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/tool')
def tool():
    return render_template('tool.html')


@app.route('/study')
def study():
    return render_template('study.html')


@app.route('/more')
def more():
    return render_template('more.html')
