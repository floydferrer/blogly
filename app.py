"""Blogly application."""

from flask import Flask, request, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, text, User, Post, Tag, PostTag

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
    posts = Post.query.order_by(Post.created_at.desc()).limit(5).all()
    return render_template('blogly.html', posts=posts)

# User Routes
@app.route('/users')
def list_users():
    users = User.query.order_by(User.first_name.asc()).all()
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
    flash(f'{first_name} {last_name} has been added', 'success')
    return redirect('/users')

@app.route('/users/<user_id>')
def view_user(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('user-page.html', user=user)

@app.route('/users/<user_id>/edit')
def edit_user(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('edit-user.html', user=user)

@app.route('/users/<user_id>/edit', methods=['POST'])
def edit_submit(user_id):
    user = User.query.get_or_404(user_id)
    user.first_name = request.form['first-name']
    user.last_name = request.form['last-name']
    user.image_url = request.form['image-url']
    db.session.add(user)
    db.session.commit()
    flash('Username has been updated', 'warning')
    return redirect('/users')

@app.route('/users/<user_id>/delete', methods=['POST'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash('User has been deleted', 'danger')
    return redirect('/users')


# Post Routes
@app.route('/posts')
def list_posts():
    users = User.query.all()
    posts = Post.query.order_by(Post.title.asc()).all()
    tags = Tag.query.all()
    return render_template('posts.html', posts=posts, users=users, tags=tags)

@app.route('/users/<user_id>/new-post')
def add_posts(user_id):
    user = User.query.get_or_404(user_id)
    tags = Tag.query.all()
    return render_template('new-post.html', user=user, tags=tags)

@app.route('/users/<user_id>/new-post', methods=['POST'])
def create_posts(user_id):
    user = User.query.get_or_404(user_id)
    title = request.form['title']
    content = request.form['content']
    tag_ids = [int(num) for num in request.form.getlist('tags')]
    tags = Tag.query.filter(Tag.id.in_(tag_ids)).all()
    new_post = Post(title=title, content=content, user=user, tags=tags)
    db.session.add(new_post)
    db.session.commit()
    flash(f'New post has been created', 'success')
    return redirect(f'/users/{user.id}')

@app.route('/users/<user_id>/post-<post_id>')
def view_posts(user_id, post_id):
    user = User.query.get_or_404(user_id)
    post = Post.query.get_or_404(post_id)
    return render_template('post-page.html', user=user, post=post)

@app.route('/users/<user_id>/post-<post_id>/edit')
def edit_post(user_id, post_id):
    user = User.query.get_or_404(user_id)
    post = Post.query.get_or_404(post_id)
    tags = Tag.query.all()
    return render_template('edit-post.html', user=user, post=post, tags=tags)

@app.route('/users/<user_id>/post-<post_id>/edit', methods=['POST'])
def update_post(user_id, post_id):
    user = User.query.get_or_404(user_id)
    post = Post.query.get_or_404(post_id)
    post.title = request.form['title']
    post.content = request.form['content']
    tag_ids = [int(num) for num in request.form.getlist('tags')]
    post.tags = Tag.query.filter(Tag.id.in_(tag_ids)).all()
    db.session.add(post)
    db.session.commit()
    flash('Post has been updated', 'warning')
    return redirect(f'/users/{user.id}/post-{post.id}')

@app.route('/users/<user_id>/post-<post_id>/delete', methods=['POST'])
def delete_post(user_id, post_id):
    user = User.query.get_or_404(user_id)
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    flash('Post has been deleted', 'danger')
    return redirect(f'/users/{user.id}')


# Tag Routes
@app.route('/tags')
def view_tags():
    tags = Tag.query.all()
    return render_template('tags.html', tags=tags)

@app.route('/tags/<tag_id>')
def view_posts_by_tag(tag_id):
    tag = Tag.query.get_or_404(tag_id)
    return render_template('tag-page.html', tag=tag)

@app.route('/tags/add')
def add_tag():
    posts = Post.query.all()
    return render_template('new-tag.html', posts=posts)

@app.route('/tags/add', methods=['POST'])
def create_tag():
    tag = request.form['tag']
    post_ids = [int(num) for num in request.form.getlist('posts')]
    posts = Post.query.filter(Post.id.in_(post_ids)).all()
    new_tag = Tag(name=tag, posts=posts)
    db.session.add(new_tag)
    db.session.commit()
    flash(f'{tag} tag has been created', 'success')
    return redirect ('/tags')

@app.route('/tags/<tag_id>/edit')
def edit_tag(tag_id):
    tag = Tag.query.get_or_404(tag_id)
    posts = Post.query.all()
    return render_template('edit-tag.html', tag=tag, posts=posts)

@app.route('/tags/<tag_id>/edit', methods=['POST'])
def update_tag(tag_id):
    tag = Tag.query.get_or_404(tag_id)
    tag.name = request.form['tag']
    post_ids = [int(num) for num in request.form.getlist('posts')]
    tag.posts = Post.query.filter(Post.id.in_(post_ids)).all()
    db.session.add(tag)
    db.session.commit()
    flash('Tag has been updated', 'warning')
    return redirect (f'/tags/{tag.id}')

@app.route('/tags/<tag_id>/delete', methods=['POST'])
def delete_tag(tag_id):
    tag = Tag.query.get_or_404(tag_id)
    db.session.delete(tag)
    db.session.commit()
    flash('Tag has been deleted', 'danger')
    return redirect(f'/tags')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404