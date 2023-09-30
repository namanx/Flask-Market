from market import app
from flask import render_template
from market.models import Item
from market.forms import RegisterForm
@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html',page='home')

@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html',items=items,page='market')

@app.route('/register')
def register():
    forms = RegisterForm()
    return render_template('register.html',form = forms,page='register')