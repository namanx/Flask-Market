from market import app,db
from flask import render_template, redirect, url_for
from market.models import Item,User
from market.forms import RegisterForm
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
                              password_hash = form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market_page'))

    # if there are no errors
    if form.errors != {}:
        for err_msg in form.errors.values():
            print(f'The error while creating user : {err_msg}')

    return render_template('register.html',form = form,page='register')