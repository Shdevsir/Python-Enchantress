from flask import request
from datetime import datetime
from store.db.database import USERS_DATABASE, user_counter
from store.errors.no_such_cart import NoSuchCart
from store.errors.no_such_user import NoSuchUser
from flask_restful import Resource


class Users(Resource):
    def post(self):
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

    def get(self, user_id):
        try:
            user = USERS_DATABASE[user_id]
        except KeyError:
            raise NoSuchUser(user_id)
        else:
            return user

    def put(self, user_id):
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

    def delete(self, user_id):
        try:
            del USERS_DATABASE[user_id]
        except KeyError:
            raise NoSuchUser(user_id)
        else:
            response = {"status": "success"}
            return response, 200
