from flask import render_template
from app import app
from app.forms import LoginForm

# ...

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
@app.route('/index')
def index():
    user = {'username': 'Chad'}
    posts = [
        {
            'author': {'username': 'Sub-5 black piller'},
            'body': 'Its all over for me'
        },
        {
            'author': {'username': 'Weakest white piller'},
            'body': 'You may be cooked, but thats ok. you must stay strong and make the most of your situation king.'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

