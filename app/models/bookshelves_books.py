from .db import db
import os
environment = os.getenv("FLASK_ENV")

# ... imports
def add_prefix_for_prod(attr):
    if environment == "production":
        return 'badreadstest' + '.' + attr
    else:
        return attr
# ...

bookshelves_books = db.Table(
    "bookshelves_books",
    db.Column(
        "book_id",
        db.Integer,
        db.ForeignKey(add_prefix_for_prod('books.id')),
        primary_key=True
    ),
    db.Column(
        "bookshelf_id",
        db.Integer,
        db.ForeignKey(add_prefix_for_prod('bookshelves.id')),
        primary_key=True
    )
)

# Add prefix to all foreign key column references in all model files

# book_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('books.id')))