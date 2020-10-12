from flask import render_template, redirect, flash, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from .model.models import User
from application import appp
from .UserDAC import db
from .forms import LoginForm, RegistrationForm, EditProfileForm
from werkzeug.urls import url_parse


@appp.route("/contact")
@login_required
def contact():
    return render_template('contact.html', blog=True)

@appp.route('/')
def redir():
    return redirect('/index')


@appp.route("/index")
@appp.route("/home")
def index():
    return render_template('index.html', index=True)


@appp.route("/near")
@login_required
def school_near_me():
    return render_template('snme.html', blog=True)


@appp.route("/about")
@login_required
def about_us():
    return render_template('about.html', blog=True)

@appp.route("/schools")
@login_required
def apply():
    return render_template('products.html', blog=True)


@appp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@appp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@appp.route("/skl")
def skl():
    #from .services.map import main
    #main()
    return render_template('Skl.html')


@appp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@appp.route('/user/<username>')
@login_required
def user(username):
    form = EditProfileForm()
    user = User.query.filter_by(username=username).first_or_404()
    if username[-3:] == 'edu':
        return render_template('schooldash.html, user=user')
    return render_template('user.html', user=user, form=form)
