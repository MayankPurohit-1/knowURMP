from Model.UserModel import UserModel
from flask_restful import Resource
from flask import request, render_template, make_response, url_for
from forms import RegistrationForm, LoginForm


class RegisterUser(Resource):
    def get(self):
        form = RegistrationForm()
        return make_response(render_template('register_form.html', form=form))

    def post(self):
        data = request.form
        user = UserModel()
        return user.register_user(data['first_name'], data['last_name'], data['email'], data['password'],
                                  data['constituency'])


class LoginUser(Resource):
    def get(self):
        form = LoginForm()
        return make_response(render_template('login_form.html', form=form))

    def post(self):
        data = request.form
        print(data)
        user = UserModel()
        return user.login_user(data['email'], data['password'], data['next'])
