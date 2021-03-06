from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = "8198926847042665"
posts = [
    {
        'author': 'Nafis ishtiaque',
        'title': 'Blog post 1',
        "content": "first post content",
        'date_posted': "april 20,2018"
    }

]


@app.route('/')  # this is the home
@app.route('/home')  # this is means its the home
def home():
    return render_template('home.html', posts=posts)


# in here post is being passed to post.
# vatirable will have access to it
@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)


@app.route("/login")
def register():
    form = LoginForm()
    return render_template('login.html', title='login', form=form)


@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
