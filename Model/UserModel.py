from database import mp_data, user_data
from datetime import datetime
from flask_jwt_extended import create_access_token
from flask import jsonify, redirect, url_for, request
from passlib.hash import sha256_crypt


class UserModel:
    SEAT = []

    def register_user(self, first_name, last_name, email,
                      password, constituency):

        result = user_data.count({"email": email})
        if result:
            return {
                "msg": "User with given email already exists! Try logging in!"
            }
        else:
            temp =mp_data.find()
            for x in temp:
                UserModel.SEAT.append(x['Constituency'])

            if constituency in UserModel.SEAT:
                result = user_data.insert_one({
                    "first_name": first_name,
                    "last_name": last_name,
                    "email": email,
                    "password": sha256_crypt.encrypt(password),
                    "constituency": constituency,
                    "created_by": datetime.utcnow()
                })

            if result:
                return redirect(url_for('loginuser'))
            else:
                return {
                    "msg": "An Error has occurred!"
                }

    @classmethod
    def find_by_email(cls, email):
        result = user_data.find_one({"email": email})
        return result

    def login_user(self, email, password, next_url):
        result = user_data.find_one({"email": email})
        if result:
            if sha256_crypt.verify(password, result['password']):
                access_token = create_access_token(identity=email)
                print(access_token)
                if next_url:
                    print(next_url)
                    query = next_url[27:]
                    query = query.replace("%20", " ")
                    print(query)
                    return redirect(url_for('afterlogin'))
                else:
                    return redirect(url_for('home'))
            else:
                return {
                    "msg": "Invalid credentials"
                }
        else:
            return {
                "msg": "Email is not registered"
            }
