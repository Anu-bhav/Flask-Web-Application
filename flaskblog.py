from flask import Flask, escape, request, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'author': 'John Doe',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'Febuary 20, 2020',
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'Febuary 21, 2020',
    },
    {
        'author': 'Sam Smith',
        'title': 'Blog Post 3',
        'content': 'Third post content',
        'date_posted': 'Febuary 22, 2020',
    },
]


@app.route('/')
@app.route('/home')
# def home():
#     name = request.args.get("name", "Anubhav")
#     return f'<h1>Hello, {escape(name)}!</h1>'
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
