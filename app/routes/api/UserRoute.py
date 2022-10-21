from flask import Blueprint
from controllers.api.UserController import show

user_route = Blueprint('user_route', __name__)

user_route.route('/<int:user_id>', methods=['GET'])(show)