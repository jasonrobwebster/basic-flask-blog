from src.common.database import Database
from src.models.blog import Blog

from flask import Flask, render_template, request, make_response, url_for, redirect

app = Flask(__name__)

@app.before_first_request
def init_db():
    Database.initialize()

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/blogs/new', methods=['GET', 'POST'])
def new_blog():
    if request.method == 'GET':
        return render_template("new_blog.html")
    else:
        title = request.form['title']
        description = request.form['description']

        new_blog = Blog(title, description)
        new_blog.save_to_mongo()

        return redirect('/')

@app.route('/blogs')
def view_blogs():
    blogs = Blog.get_blogs()
    return render_template("view_blogs.html", blogs=blogs)

@app.route('/posts/<string:blog_id>')
def view_blog_posts(blog_id):
    blog = Blog.from_mongo(blog_id)
    posts = blog.get_posts()
    return render_template('view_posts.html', posts=posts, blog_id=blog._id, blog_title=blog.title, blog_description=blog.description)

@app.route('/posts/new/<string:blog_id>', methods=['GET', 'POST'])
def new_post(blog_id):
    if request.method == 'GET':
        return render_template('new_post.html', blog_id=blog_id)
    else:
        title = request.form['title']
        abstract = request.form['abstract']
        content = request.form['content']

        blog = Blog.from_mongo(blog_id)
        blog.new_post(title, abstract, content)

        return redirect(f'/posts/{blog_id}')

@app.route('/posts/<string:blog_id>/<string:post_id>')
def view_post(blog_id, post_id):
    blog = Blog.from_mongo(blog_id)
    post = blog.get_post(post_id)

    return render_template("view_post.html", blog_title=blog.title, blog_id=blog._id, post=post)

if __name__ == '__main__':
    app.run(debug=True)
