from flask import render_template, request, redirect, url_for, Blueprint
from .forms import registrationForm, loginForm
from ..models import User

users = Blueprint('users', __name__)

@users.route('/register', methods=['GET', 'POST'])
def registerUserPage():
    form = registrationForm()
    if request.method == 'POST':
        if form.validate_on_submit:
            username = form.username.data
            email = form.username.data
            password = form.password.data
            print(username, email, password)


            return redirect(url_for('users.loginUserPage'))
    return render_template('register.html', form = form)

@users.route('/login', methods=['GET', 'POST'])
def loginUserPage():
    form = loginForm()
    
    return render_template('login.html', form = form)