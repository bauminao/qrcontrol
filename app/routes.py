from flask import render_template, flash, redirect, url_for
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", title='QR-control')

@app.route('/')
@app.route('/connect')
def index():
    return render_template("connect.html", title='QR-control')
