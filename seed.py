from models import db, connect_db, text, User, Post, Tag, PostTag
from app import app

db.drop_all()
db.create_all()

u1 = User(first_name='sans', last_name='da skeleton', image_url='https://static.wikia.nocookie.net/characterprofile/images/0/01/Sans_undertale.jpg')
u2 = User(first_name='PAPYRUS', last_name='da skeleton', image_url='https://static.wikia.nocookie.net/characterprofile/images/d/d3/Papyrus1.png')
u3 = User(first_name='Ralsei', last_name='Dreemur', image_url='https://static.wikia.nocookie.net/deltarune/images/5/5c/Ralsei_face_hatless.png')
u4 = User(first_name='Starlo', last_name='UTY', image_url='https://static.wikia.nocookie.net/undertaleyellow/images/a/a3/Starlo_battle_idle.gif')

db.session.add_all([u1, u2, u3, u4])

db.session.commit()

p1 = Post(title='Megalovania', content="It's a beautiful day outside...", user_id=1)
p2 = Post(title='Bad Pun', content="Why don't zombies like to eat comedians? Because they taste funny.", user_id=1)
p3 = Post(title='The Great Papyrus', content="My name is Papyrus of the legendary royal guard. Nyeh heh heh", user_id=2)
p4 = Post(title='Special Attack', content="Toby, come back here with my special attack!!! ...Well, here's a really cool normal attach then.", user_id=2)
p5 = Post(title='Bruh.', content="I'm good, you can do section 3 without me. I'm going to chill here all game.", user_id=3)
p6 = Post(title='Duck joke', content="Why do ducks have butt feathers? to cover their butt quack! AHAHAHAHAHAHAHA", user_id=4)
p7 = Post(title='another joke', content="Why did the chicken cross the playground? to get to the other slide!", user_id=4)
p8 = Post(title='pasta joke', content="What happened to the ghost chef? He pasta-way!", user_id=4)

db.session.add_all([p1, p2, p3, p4, p5, p6, p7, p8])
db.session.commit()

t1 = Tag(name='hilarious')
t2 = Tag(name='dangerous')
t3 = Tag(name='powerful')
t4 = Tag(name='legendary')
t5 = Tag(name='bruh')
t6 = Tag(name='arf')
t7 = Tag(name='nyeh-heh-heh')
t8 = Tag(name='doggy')
t9 = Tag(name='skelebro')

db.session.add_all([t1, t2, t3, t4, t5, t6, t7, t8, t9])
db.session.commit()

pt1 = PostTag(post_id=1, tag_id=2)
pt2 = PostTag(post_id=1, tag_id=3)
pt3 = PostTag(post_id=1, tag_id=4)
pt4 = PostTag(post_id=2, tag_id=1)
pt5 = PostTag(post_id=2, tag_id=5)
pt6 = PostTag(post_id=3, tag_id=3)
pt7 = PostTag(post_id=3, tag_id=4)
pt8 = PostTag(post_id=3, tag_id=7)
pt9 = PostTag(post_id=4, tag_id=2)
pt10 = PostTag(post_id=4, tag_id=3)
pt11 = PostTag(post_id=5, tag_id=5)
pt12 = PostTag(post_id=6, tag_id=1)
pt13 = PostTag(post_id=6, tag_id=5)
pt14 = PostTag(post_id=7, tag_id=1)
pt15 = PostTag(post_id=8, tag_id=1)
pt16 = PostTag(post_id=8, tag_id=5)

db.session.add_all([pt1, pt2, pt3, pt4, pt5, pt6, pt7, pt8, pt9, pt10, pt11, pt12, pt13, pt14, pt15, pt16])
db.session.commit()