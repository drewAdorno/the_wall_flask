from crypt import methods
from flask import render_template, redirect, request, session, flash
from flask_app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    return render_template('index.html')
