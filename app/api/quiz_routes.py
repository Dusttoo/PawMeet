from flask import Blueprint, jsonify, request
from app.models import User_Answer, db
from app.forms.user_answer import UserAnswerForm


quiz_routes = Blueprint('quiz', __name__)


@quiz_routes.route('/<int:id>')
def answers(id):
    answers = User_Answer.query.filter_by(user_id=id)
    return {'answers': [answer.to_dict() for answer in answers]}


@quiz_routes.route('/add', methods=['POST'])
def submit_answers():
    if request.method == "POST":
        form = UserAnswerForm()
        form['csrf_token'].data = request.cookies['csrf_token']
        if form.validate_on_submit():
            data = User_Answer()
            form.populate_obj(data)
            db.session.add(data)
            db.session.commit()
            return data.to_dict()


@quiz_routes.route('<int:id>/delete', methods=['DELETE'])
def delete_quiz(id):

    db.session.query(User_Answer).filter_by(user_id=id).delete()
    db.session.commit()

    return {'deleted': id}
