from flask import Blueprint, jsonify, request
from app.models import User_Answer, db
from app.forms.add_pet import PetForm


pet_routes = Blueprint('pets', __name__)


@pet_routes.route('')
def pets():
    pets = Pet_Profile.query.all()
    return {'pets': [pet.to_dict() for pet in pets]}


@pet_routes.route('/add', methods=['POST'])
def add_pet():
    if request.method == "POST":
        form = PetForm()
        form['csrf_token'].data = request.cookies['csrf_token']
        if form.validate_on_submit():
            data = Pet_Profile()
            print('\n\n\n pet data', data, '\n\n\n')
            form.populate_obj(data)
            db.session.add(data)
            db.session.commit()
            return data.to_dict()
