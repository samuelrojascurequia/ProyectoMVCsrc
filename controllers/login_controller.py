from flask import render_template, request
from flask_controller import FlaskController 
from src.app import app

class LoginController():    
    @app.route ('/login')
    def login_html():
        return render_template('login.html')
