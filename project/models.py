# project/models.py
from project import db

class Post(db.Model):
    __tablename__ = 'post'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    text = db.Column(db.Text, nullable=False)

    def __init__(self, title, text):
        self.title = title
        self.text = text

    def __repr__(self):
        return f"<Post {self.title}>"
