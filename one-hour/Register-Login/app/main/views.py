from flask import render_template
from . import main

history_list = []

@main.route('/')
def index():
    return render_template('index.html')