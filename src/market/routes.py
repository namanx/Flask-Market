from market import app,db
from flask import render_template, redirect, url_for,flash
from market.models import Item,User
from market.forms import RegisterForm,LoginForm
from flask_login import login_user


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html',page='home')

@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html',items=items,page='market')

@app.route('/register',methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username = form.username.data,
                              email_address = form.email_address.data,
                              password = form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market_page'))

    # if there are no errors
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'The error while creating user : {err_msg}',category='danger')

    return render_template('register.html',form = form,page='register')

@app.route('/login',methods=['GET','POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username = form.username.data).first()
        try:
            if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
                login_user(attempted_user)
                flash(f"Success ! You are logged in as user : {attempted_user.username}",category='success')
                return redirect(url_for('market_page'))
    

            else:
                flash("Username and password is not matched please try again",category='danger')
        except:
            flash("Username and password is not matched please try again",category='danger')


    return render_template('login.html',page = 'login',form=form)