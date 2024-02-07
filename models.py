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
 
    image_url = db.Column(db.String(200),
                           nullable=False)
    
    posts = db.Relationship('Post', backref='user')

    @classmethod
    def get_by_user_id(cls, user_id):
        return cls.query.get(user_id)

class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)

    title = db.Column(db.String(30),
                           nullable=False)
    
    content = db.Column(db.String(500),
                           nullable=False)
 
    created_at = db.Column(db.DateTime(), default=datetime.datetime.now,
                           nullable=False)
    
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'), nullable=False)

    @classmethod
    def get_by_post_id(cls, post_id):
        return cls.query.get(post_id)
    
