from models import db, connect_db, text, User, Post
from app import app

db.drop_all()
db.create_all()

u1 = User(first_name='sans', last_name='da skeleton', image_url='https://static.wikia.nocookie.net/characterprofile/images/0/01/Sans_undertale.jpg')
u2 = User(first_name='PAPYRUS', last_name='da skeleton', image_url='https://static.wikia.nocookie.net/characterprofile/images/d/d3/Papyrus1.png')
u3 = User(first_name='Ralsei', last_name='Dreemur', image_url='https://static.wikia.nocookie.net/deltarune/images/5/5c/Ralsei_face_hatless.png')

db.session.add_all([u1, u2, u3])

db.session.commit()

p1 = Post(title='Megalovania', content='Wanna have a bad time?', user_id=1)

db.session.add(p1)
db.session.commit()