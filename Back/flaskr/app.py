from flaskr import create_app
from flask import jsonify
from .modelos import *
from .vistas import *
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_cors import CORS

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

CORS = CORS(app)

api = Api(app)
api.add_resource(SignIn, '/api/auth/signup')
api.add_resource(LogIn, '/api/auth/login')
api.add_resource(GetTasks, '/api/tasks')
api.add_resource(UploadFile, '/api/tasks')
api.add_resource(SaveTask,'/api/save')
api.add_resource(GetTask, '/api/tasks/<int:id_task>')
api.add_resource(Delete, '/api/delete/<int:id_task>')

jwt = JWTManager(app)
