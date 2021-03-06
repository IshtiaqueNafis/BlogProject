from flask import Flask, render_template,url_for

app = Flask(__name__)
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
    return render_template('home.html',posts=posts,title='test')
# in here post is being passed to post.
#vatirable will have access to it



@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
