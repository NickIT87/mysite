from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm


# no import ! need to check
app = Flask(__name__)

app.config['SECRET_KEY'] = 'e09920cde250dbd5e37781ed1326db5f'

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 20, 2020'
    }
]

@app.route("/")
@app.route("/home/")
def home():
    return render_template("home.html", posts=posts, title='Home')

@app.route("/about")
def about():
    return render_template("about.html", title='About')

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = RegistrationForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)