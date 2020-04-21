from flask import Flask
from flask_restful import Api
from Resource.User import RegisterUser, LoginUser
from Resource.MP import ListMP, Home


app = Flask(__name__)
app.config['SECRET_KEY'] = 'masterkey'
api = Api(app)


api.add_resource(RegisterUser, '/register')
api.add_resource(LoginUser, '/login')
api.add_resource(ListMP, '/search')
api.add_resource(Home, '/')


app.run(debug=True, port=5000)
