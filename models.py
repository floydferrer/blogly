import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)

    first_name = db.Column(db.String(20),
                           nullable=False)
    
    last_name = db.Column(db.String(20),
                           nullable=False)
 
    image_url = db.Column(db.String(500),
                           nullable=False)
    
    posts = db.Relationship('Post', cascade='all, delete', backref='user')

    @classmethod
    def get_by_user_id(cls, user_id):
        return cls.query.get(user_id)
    
    def __repr__(self):
        return f'<User {self.first_name} {self.last_name}>'

class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)

    title = db.Column(db.String(40),
                           nullable=False)
    
    content = db.Column(db.String(500),
                           nullable=False)
 
    created_at = db.Column(db.DateTime, default=datetime.datetime.now,
                           nullable=False)
    
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'), nullable=False)

    @classmethod
    def get_by_post_id(cls, post_id):
        return cls.query.get(post_id)
    
    @property
    def friendly_time(self):
        return self.created_at.strftime('%a %b %-d %Y, %-I:%M %p')
    
    def __repr__(self):
        return f'<Post {self.id} {self.title}>'

class PostTag(db.Model):
    __tablename__ = 'post_tags'

    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), primary_key=True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'), primary_key=True)
    
class Tag(db.Model):
    __tablename__ = 'tags'

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)

    name = db.Column(db.String(30),
                           nullable=False,
                           unique=True)
    
    posts = db.Relationship('Post', secondary='post_tags', backref='tags')
    

    @classmethod
    def get_by_tag_id(cls, tag_id):
        return cls.query.get(tag_id)
    
    def __repr__(self):
        return f'<Tag {self.id} {self.name}>'

