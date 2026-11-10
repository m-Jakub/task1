from project import db, app
from sqlalchemy.orm import validates
import re


# Book model
class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    author = db.Column(db.String(64))
    year_published = db.Column(db.Integer) 
    book_type = db.Column(db.String(20))
    status = db.Column(db.String(20), default='available')

    def __init__(self, name, author, year_published, book_type, status='available'):
        self.name = name
        self.author = author
        self.year_published = year_published
        self.book_type = book_type
        self.status = status

    def __repr__(self):
        return f"Book(ID: {self.id}, Name: {self.name}, Author: {self.author}, Year Published: {self.year_published}, Type: {self.book_type}, Status: {self.status})"

    @validates('author') # za każdym razem gdy kod próbuje przypisać wartość do pola author, wywołuje się ta metoda
    def validate_author(self, key, author):
        if not author:
            raise ValueError("Author name cannot be empty.")
        if len(author) > 64:
            raise ValueError("Author name cannot exceed 64 characters.")
        if not re.match(r'^[a-zA-ZąćęłńóśźżĄĆĘŁŃÓŚŹŻàâäéèêëîïôöùûüÿçÀÂÄÉÈÊËÎÏÔÖÙÛÜŸÇ\s\.\-\'\,]+$', author):
            raise ValueError("Author name contains invalid characters.")
        return author


with app.app_context():
    db.create_all()