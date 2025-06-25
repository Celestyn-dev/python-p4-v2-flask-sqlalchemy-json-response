# server/seed.py

from app import app
from models import db, Pet

with app.app_context():
    Pet.query.delete()

    pets = [
        Pet(name="Robin", species="Hamster"),
        Pet(name="Gwendolyn", species="Dog"),
        Pet(name="Michael", species="Turtle"),
        Pet(name="Austin", species="Cat"),
        Pet(name="Jennifer", species="Dog"),
        Pet(name="Jenna", species="Dog"),
        Pet(name="Crystal", species="Chicken"),
        Pet(name="Jacob", species="Cat"),
        Pet(name="Nicole", species="Chicken"),
        Pet(name="Trevor", species="Turtle"),
    ]

    db.session.add_all(pets)
    db.session.commit()
