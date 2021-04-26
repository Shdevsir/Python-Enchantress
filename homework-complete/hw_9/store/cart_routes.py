from flask import request
from datetime import datetime
from store.db.database import CART_DATABASE, cart_counter, user_counter
from store.errors.no_such_cart import NoSuchCart
from store.errors.no_such_user import NoSuchUser
from flask_restful import Resource


class Carts(Resource):
    def post(self):
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

    def get(self, cart_id):
        try:
            cart = CART_DATABASE[cart_id]
        except KeyError:
            raise NoSuchCart(cart_id)
        else:
            return cart

    def put(self, cart_id):
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

    def delete(self, cart_id):
        try:
            del CART_DATABASE[cart_id]
        except KeyError:
            raise NoSuchCart(cart_id)
        else:
            response = {"status": "success"}
            return response, 200
