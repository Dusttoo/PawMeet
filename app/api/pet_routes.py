from flask import Blueprint, jsonify, request
from app.models import Pet_Profile, Pet_Image, db
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


@pet_routes.route('/<int:id>/edit', methods=['POST'])
def edit_pet(id):
    form = PetForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        data = form.data
        pet = Pet_Profile.query.get(id)
        pet.user_id = data['user_id']
        pet.profile_img = data['profile_img']
        pet.name = data['name']
        pet.breed = data['breed']
        pet.age = data['age']
        pet.description = data['description']
        db.session.commit()
        return pet.to_dict()


@pet_routes.route('<int:id>/delete', methods=['DELETE'])
def delete_pet(id):

    pet = Pet_Profile.query.get(id)
    db.session.delete(pet)
    db.session.commit()

    return pet.to_dict()
