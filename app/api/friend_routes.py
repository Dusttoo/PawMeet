from flask import Blueprint
from app.models import Friend_Request, Friends_List
from app.forms.friend_request import AddFriendForm
from app.forms.friends_list_form import FriendListForm

friend_routes = Blueprint('friends', __name__)


def validation_errors_to_error_messages(validation_errors):
    """
    Simple function that turns the WTForms validation errors into a simple list
    """
    errorMessages = []
    for field in validation_errors:
        for error in validation_errors[field]:
            errorMessages.append(f'{field} : {error}')
    return errorMessages

@friend_routes.route('/<int:id>/requests')
def requests(id):
    requests = Friend_Request.query.filter(Friend_Request.user_id_from == id or 
                                        Friend_Request.user_id_to == id)
    return {'requests': [request.to_dict() for request in requests]}


@friend_routes.route('/<int:id>/friends')
def friends(id):
    friends = Friends_List.query.filter(Friends_List.current_user_id == id)
    return {'friends': [friend.to_dict() for friend in friends]}