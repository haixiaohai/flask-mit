from flask import render_template, flash, redirect, url_for, request
from app import webapp, login, db
from app.forms import LoginForm, RegisterForm, SingleForm,SingleForm1,SingleForm2
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from werkzeug.urls import url_parse
from app.maipulib import *


@webapp.route('/', methods=['POST', 'GET'])
@webapp.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    return render_template('index.html')


@webapp.route('/single',methods=['GET','POST'])
def single():
    form = SingleForm()
    if request.method == 'POST':
        if form.login_type.data == 'telnet':
            device = TConnection(host=form.ipaddress.data,
                                 password=form.password.data,
                                 username=form.username.data,
                                 enable_password=form.enable_password.data)
            device.connect()
            device.exec('show version')
                

            return redirect(url_for('single'))
        else:
            device = SConnection(host=form.ipaddress.data,
                                 password=form.password.data,
                                 username=form.username.data,
                                 enable_password=form.enable_password.data)
            device._connect()

            return redirect(url_for('single'))
    return render_template('single.html', form=form)


@webapp.route('/batch')
def batch():
    return render_template('batch.html')


@webapp.route('/config')
def config():
    return render_template('config.html')

@webapp.route('/new')
def new():
    return render_template('new.html')

@webapp.route('/login', methods=['GET', 'POST'])
def sign_in():
    if current_user.is_authenticated:
        redirect(url_for('index'))
    loginform = LoginForm()
    if loginform.validate_on_submit():
        user = User.query.filter_by(username=loginform.username.data).first()
        if user is None:
            flash('username is not exists,please register.')
        elif not user.check_password(loginform.password.data):
            flash('Invalid Password')
        else:
            login_user(user)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('index')
            return redirect(next_page)
    return render_template('login.html', title='Sign In', form=loginform)


@webapp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        redirect(url_for('index'))
    registerform = RegisterForm()
    if registerform.validate_on_submit():
        user = User(username=registerform.username.data)
        user.password_set(registerform.password.data)
        db.session.add(user)
        db.session.commit()
        flash('register success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=registerform)


@webapp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('sign_in'))


@webapp.route('/about')
def about():
    return  render_template('about.html') 


@webapp.route('/test')
def boot():
    return render_template('boot.html')