from flask import Blueprint, jsonify, request
from app.models import Breed_Group, Breed, Breed_Image, Breed_Answer, Breed_Trait, db
from app.forms.add_pet import PetForm


breed_routes = Blueprint('breeds', __name__)


@breed_routes.route('/groups')
def groups():
    groups = Breed_Group.query.all()
    return {'groups': [group.to_dict() for group in groups]}


@breed_routes.route('')
def breeds():
    breeds = Breed.query.all()
    return {'breeds': [breed.to_dict() for breed in breeds]}


@breed_routes.route('/traits')
def traits():
    traits = Breed_Trait.query.all()
    return {'traits': [trait.to_dict() for trait in traits]}


@breed_routes.route('/images')
def images():
    images = Breed_Image.query.all()
    return {'images': [image.to_dict() for image in images]}


@breed_routes.route('/answers')
def answers():
    answers = Breed_Answer.query.all()
    return {'awnsers': [answer.to_dict() for answer in answers]}
