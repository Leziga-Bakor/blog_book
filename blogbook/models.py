from flask import current_app
from datetime import datetime, timezone, timedelta
from itsdangerous import URLSafeTimedSerializer as Serializer
from authlib.jose import jwt
from blogbook import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file=db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts=db.relationship('Post', backref='author', lazy=True)

    def get_reset_token(self, expires_sec=1800):
        header = {'alg':'HS256'}
        payload = {
            'user_id':self.id,
            'exp': datetime.now(timezone.utc) + timedelta(seconds=expires_sec)
        }
        token = jwt.encode(header, payload, current_app.config['SECRET_KEY'])
        return token.decode('utf-8')
    
    @staticmethod
    def verify_reset_token(token):
        try:
            claims = jwt.decode(token, current_app.config['SECRET_KEY'])
            claims.validate()
            user_id = claims['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"
    
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default = datetime.now(timezone.utc))
    content = db.Column(db.Text, nullable=False)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}','{self.date_posted}')"