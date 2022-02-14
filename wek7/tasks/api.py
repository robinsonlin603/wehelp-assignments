from flask import *
from flask_restful import Api, Resource
from mysql.connector import pooling
api_blueprints = Blueprint(
    "api",
    __name__,
)
connection = pooling.MySQLConnectionPool(
    pool_name = "pynative_pool",
    pool_size = 5,
    pool_reset_session = True,
    host = "localhost",
    database = "member_system",
    user = "root",
    password = "goodtime123"
)
connection_object = connection.get_connection()
db_Info = connection_object.get_server_info()
api = Api(api_blueprints)

# API 查詢系統

class ResearchUser(Resource):
    def get(self):
        with connection_object.cursor(dictionary=True) as cursor:
            username = request.args.get("username")
            cursor.execute("SELECT `id`,`name`,`email` FROM `member` where email=%s",[username])
            result = cursor.fetchone()
            if result !=None:
                return {"data":result}
            else:
                return {"data":{"name":"查無此人"}}

# API 修改系統

class ChangeName(Resource):
    def post(self):
        id = session["id"]
        with connection_object.cursor(dictionary=True) as cursor:
            content_type = request.headers.get('Content-Type')
            if (content_type == 'application/json'):
                newname = request.json["name"]
                cursor.execute("UPDATE `member` SET `name`=%s WHERE `id`=%s",[newname,id])
                connection_object.commit()
                session["name"] = newname
                return {"ok":True}
            else:
                return {"error":True}

api.add_resource(ChangeName,"/api/member")
api.add_resource(ResearchUser,"/api/members")