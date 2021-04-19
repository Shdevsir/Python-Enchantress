from flask import Flask, request
from datetime import datetime

amazon_killer = Flask(__name__)

CART_DATABASE = {}
USERS_DATABASE = {}
user_counter = 1
cart_counter = 1


class NoSuchCart(Exception):
    def __init__(self, cart_id):
        self.cart_id = cart_id


class NoSuchUser(Exception):
    def __init__(self, user_id):
        self.user_id = user_id


@amazon_killer.route('/users', methods=["POST"])
def create_user():
    global user_counter
    user = request.json
    user['user_id'] = user_counter
    response = {
        "registration_timestamp": datetime.now().isoformat(),
        "user_id": user_counter
    }
    user["registration_timestamp"] = response['registration_timestamp']
    USERS_DATABASE[user_counter] = user

    user_counter += 1

    return response, 201


@amazon_killer.errorhandler(NoSuchUser)
def no_such_user_handler(e):
    return {"error": f"no such user with id {e}"}, 404


@amazon_killer.errorhandler(NoSuchCart)
def no_such_cart_handler(e):
    return {"error": f"no such cart with id {e}"}, 404


@amazon_killer.route('/users/<int:user_id>')
def get_user(user_id):
    try:
        user = USERS_DATABASE[user_id]
    except KeyError:
        raise NoSuchUser(user_id)
    else:
        return user


@amazon_killer.route('/users/<int:user_id>', methods=["PUT"])
def put_user(user_id):
    data = request.json
    try:
        USERS_DATABASE[user_id].update(
            {
                "name": data["name"],
                "email": data["email"]
            }
        )
    except KeyError:
        raise NoSuchUser(user_id)
    else:
        response = {"status": "success"}
        return response, 200


@amazon_killer.route('/users/<int:user_id>', methods=["DELETE"])
def delete_user(user_id):
    try:
        del USERS_DATABASE[user_id]
    except KeyError:
        raise NoSuchUser(user_id)
    else:
        response = {"status": "success"}
        return response, 200


@amazon_killer.route('/carts', methods=["POST"])
def create_cart():
    global cart_counter
    cart = request.json
    try:
        cart['cart_id'] = cart_counter
        response = {
            "creation_time": datetime.now().isoformat(),
            "cart_id": cart_counter
        }
        cart["creation_time"] = response['creation_time']
        CART_DATABASE[cart_counter] = cart
        cart['user_id'] = user_counter
    except KeyError:
        raise NoSuchUser(cart['user_id'])
    else:
        cart_counter += 1
        return response, 201


@amazon_killer.route('/carts/<int:cart_id>')
def get_cart(cart_id):
    try:
        cart = CART_DATABASE[cart_id]
    except KeyError:
        raise NoSuchCart(cart_id)
    else:
        return cart


@amazon_killer.route('/carts/<int:cart_id>', methods=["PUT"])
def put_cart(cart_id):
    try:
        data = request.json
        CART_DATABASE[cart_id].update(
            {
                "user_id": data["user_id"],
                "procucts": data["products"]
            }
        )
    except KeyError:
        raise NoSuchCart(cart_id)
    else:
        response = {"status": "success"}
        return response, 201


@amazon_killer.route('/carts/<int:cart_id>', methods=["DELETE"])
def del_cart(cart_id):
    try:
        del CART_DATABASE[cart_id]
    except KeyError:
        raise NoSuchCart(cart_id)
    else:
        response = {"status": "success"}
        return response, 200


if __name__ == '__main__':
    amazon_killer.run(debug=True)
