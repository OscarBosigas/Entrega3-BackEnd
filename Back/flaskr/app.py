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
api.add_resource(CompressZip, '/api/tasks/zip')
api.add_resource(CompressRar, '/api/tasks/rar')
api.add_resource(Compress7Z, '/api/tasks/7z')
api.add_resource(CompressTar, '/api/tasks/tar')
api.add_resource(GetTasks, '/api/tasks')
api.add_resource(UploadFile, '/api/tasks')
api.add_resource(SaveTask,'/api/save')
api.add_resource(GetTask, '/api/tasks/<int:id_event>')

jwt = JWTManager(app)
