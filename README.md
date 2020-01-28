# basic-flask-blog

This is a basic blog built using Python's Flask environment utilising MongoDB as a database. A single user can view all blogs, create a new blog, create posts under a bog, view all posts in a blog, and view the contents of a single post. Navigation still needs to be improved.

This blog is largely based off the [Udemy Complete Python Web Course](https://explore.udemy.com/course/the-complete-python-web-course-learn-by-building-8-apps) and this [code](https://github.com/schoolofcode-me/web_blog) written by [jslvtr](https://github.com/jslvtr).

## Getting Started

You'll need to install [MongoDB](https://www.mongodb.com/download-center/community) and run a local MongoDB server. The app assumes that the local MongoDB server will run with a URI of `mongodb://127.0.0.1:27017`.

### Installing
On macOS / linux:
```console
$ git clone https://github.com/jasonrobwebster/basic-flask-blog.git 
$ cd basic-flask-blog/
$ python3 -m venv venv/
$ source ./venv/bin/activate
$ pip install -r requirements.txt
```

On windows using git bash:
```console
$ git clone https://github.com/jasonrobwebster/basic-flask-blog.git 
$ cd basic-flask-blog/
$ python3 -m venv venv/
$ source ./venv/bin/activate
$ pip install -r requirements.txt
```

### Running
Run `python src/app.py` to launch the website, then go to `localhost:5000/` to view the website.
