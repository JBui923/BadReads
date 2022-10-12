from flask.cli import AppGroup
from .users import seed_users, undo_users
from .books_bookshelves import seed_books_bookshelves,undo_books_bookshelves
from .reviews import seed_reviews, undo_reviews
from app.models import db
import os

environment = os.getenv("FLASK_ENV")
# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
        if environment == 'production':
        # Before seeding, truncate all tables prefixed with schema name
        # Add a truncate command for each table that will be seeded.
        db.session.execute('TRUNCATE table badreadstest.users RESTART IDENTITY CASCADE;')
        db.session.execute('TRUNCATE table badreadstest.books_list RESTART IDENTITY CASCADE;')
        db.session.execute('TRUNCATE table badreadstest.reviews RESTART IDENTITY CASCADE;')
        db.session.execute('TRUNCATE table badreadstest.books_bookshelves RESTART IDENTITY CASCADE;')
        db.session.commit()
    seed_users()
    seed_books_bookshelves()
    seed_reviews()
    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_users()
    undo_books_bookshelves()
    undo_reviews()
    # Add other undo functions here
