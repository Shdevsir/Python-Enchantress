from store.cart_routes import Carts
from store.user_routes import Users
from flask import Flask
from flask_restful import Api
from store.errors.no_such_cart import NoSuchCart
from store.errors.no_such_user import NoSuchUser

amazon_killer = Flask(__name__)
api = Api(amazon_killer)


@amazon_killer.errorhandler(NoSuchUser)
def no_such_user_handler(e):
    return {"error": f"no such user with id {e}"}, 404


@amazon_killer.errorhandler(NoSuchCart)
def no_such_cart_handler(e):
    return {"error": f"no such cart with id {e}"}, 404


api.add_resource(Users, '/users', '/users/<int:user_id>')
api.add_resource(Carts, '/carts', '/carts/<int:cart_id>')


if __name__ == '__main__':
    amazon_killer.run(debug=True)
