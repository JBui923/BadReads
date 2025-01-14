from .db import db
from .bookshelves_books import bookshelves_books
import os
environment = os.getenv("FLASK_ENV")

class Bookshelf(db.Model):
    __tablename__ = "bookshelves"
    if environment == "production":
        __table_args__={'schema': 'badreadstest'}

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable=False)
    default = db.Column(db.Boolean, nullable=False)
    name = db.Column(db.String(255), nullable=False)

    user = db.relationship("User",back_populates="bookshelves")

    books = db.relationship(
        "Book",
        secondary=bookshelves_books,
        back_populates="bookshelves"
    )

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user,
            'default': self.default,
            'name': self.name,
            'books': self.books
        }
