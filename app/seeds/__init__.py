from flask.cli import AppGroup
from .users import seed_users, undo_users
from .breed_answers import seed_breed_answers, undo_breed_answers
from .breed_groups import seed_breed_groups, undo_breed_groups
from .breed_images import seed_breed_images, undo_breed_images
from .breed_traits import seed_breed_traits, undo_breed_traits
from .breeds import seed_breeds, undo_breeds
from .pet_images import seed_pet_images, undo_pet_images
from .pet_profiles import seed_pet_profiles, undo_pet_profiles
from .posts import seed_posts, undo_posts
from .comments import seed_comments, undo_comments
from .likes import seed_likes, undo_likes

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    seed_users()
    seed_breed_groups()
    seed_breeds()
    seed_breed_images()
    seed_breed_traits()
    seed_breed_answers()
    seed_pet_profiles()
    seed_pet_images()
    seed_posts()
    # seed_comments()
    seed_likes()
    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_users()
    undo_breed_groups()
    undo_breeds()
    undo_breed_images()
    undo_breed_traits()
    undo_breed_answers()
    undo_pet_profiles()
    undo_pet_images()
    undo_posts()
    undo_comments()
    undo_likes()
    # Add other undo functions here
