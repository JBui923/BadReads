from .db import db
from datetime import datetime
import os
environment = os.getenv("FLASK_ENV")

class Review(db.Model):
    __tablename__ = "reviews"
    if environment == "production":
        __table_args__={'schema': 'badreadstest'}
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id", ondelete="CASCADE")), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("books.id")), nullable=False)
    review = db.Column(db.String(1000), nullable=False)
    stars = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    user = db.relationship("User",back_populates="reviews")
    books = db.relationship("Book",back_populates="reviews")

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'book_id': self.book_id,
            'review': self.review,
            'stars': self.stars,
            'updated_at': self.updated_at,
            'created_at': self.created_at,
            'user': self.user.to_dict()
        }
