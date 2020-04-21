from flask_restful import Resource
from Model.MPModel import MPModel
from flask import request, render_template, make_response


class ListMP(Resource):
    def post(self):
        data = request.form
        mp = MPModel()
        return mp.list_mp(data['state'], data['constituency'])


class Home(Resource):
    def get(self):
        mp = MPModel()
        return mp.home()

