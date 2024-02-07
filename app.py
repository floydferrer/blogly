"""Blogly application."""

from flask import Flask, request, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, text, User, Post

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'

app.app_context().push()

app.config['SECRET_KEY'] = '12345'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

debug = DebugToolbarExtension(app)

connect_db(app)

db.create_all()

@app.route('/')
def list_home():
    users = User.query.all()
    return redirect('/users')

@app.route('/users')
def list_users():
    users = User.query.all()
    return render_template('users.html', users=users)

@app.route('/users/new')
def add_users():
    return render_template('new-user.html')

@app.route('/users/new', methods=['POST'])
def create_user():
    first_name = request.form['first-name']
    last_name = request.form['last-name']
    image_url = request.form['image-url']
    new_user = User(first_name=first_name, last_name=last_name, image_url=image_url)
    db.session.add(new_user)
    db.session.commit()
    return redirect('/users')

@app.route('/users/<user_id>')
def view_user(user_id):
    user = User.get_by_user_id(user_id)
    return render_template('user-page.html', user=user)

@app.route('/users/<user_id>/edit')
def edit_user(user_id):
    user = User.get_by_user_id(user_id)
    return render_template('edit-user.html', user=user)

@app.route('/users/<user_id>/edit', methods=['POST'])
def edit_submit(user_id):
    user = User.get_by_user_id(user_id)
    user.first_name = request.form['first-name']
    user.last_name = request.form['last-name']
    user.image_url = request.form['image-url']
    db.session.add(user)
    db.session.commit()
    return redirect('/users')

@app.route('/users/<user_id>/delete', methods=['POST'])
def delete_user(user_id):
    user = User.get_by_user_id(user_id)
    db.session.delete(user)
    db.session.commit()
    return redirect('/users')

@app.route('/users/<user_id>/new-post')
def add_posts(user_id):
    user = User.get_by_user_id(user_id)
    return render_template('new-post.html', user=user)

@app.route('/users/<user_id>/new-post', methods=['POST'])
def create_posts(user_id):
    user = User.get_by_user_id(user_id)
    title = request.form['title']
    content = request.form['content']
    new_post = Post(title=title, content=content, user_id=user.id)
    db.session.add(new_post)
    db.session.commit()
    return redirect(f'/users/{user.id}')

@app.route('/users/<user_id>/post-<post_id>')
def view_posts(user_id, post_id):
    user = User.get_by_user_id(user_id)
    post = Post.get_by_post_id(post_id)
    return render_template('view-post.html', user=user, post=post)

@app.route('/users/<user_id>/post-<post_id>/edit')
def edit_post(user_id, post_id):
    user = User.get_by_user_id(user_id)
    post = Post.get_by_post_id(post_id)
    return render_template('edit-post.html', user=user, post=post)

@app.route('/users/<user_id>/post-<post_id>/edit', methods=['POST'])
def update_post(user_id, post_id):
    user = User.get_by_user_id(user_id)
    post = Post.get_by_post_id(post_id)
    post.title = request.form['title']
    post.content = request.form['content']
    db.session.add(post)
    db.session.commit()
    return redirect(f'/users/{user.id}/post-{post.id}')

@app.route('/users/<user_id>/post-<post_id>/delete', methods=['POST'])
def delete_post(user_id, post_id):
    user = User.get_by_user_id(user_id)
    post = Post.get_by_post_id(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(f'/users/{user.id}')