from flask import *
tasks_blueprints=Blueprint(
    "tasks",
    __name__,
    template_folder="templates",
)
from mysql.connector import pooling
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
# 錯誤路由
@tasks_blueprints.route("/error")
def error():
    message = request.args.get("msg","自訂的錯誤訊息")
    return render_template("/error.html",message=message)

# 註冊路由
@tasks_blueprints.route("/signup",methods=["POST"])
def signup():
    name = request.form["name"]
    email = request.form["email"]
    password = request.form["password"]
    with connection_object.cursor() as cursor:
        cursor.execute("SELECT `email` FROM `member` WHERE `email`=%s",[email])
        result=cursor.fetchone()
        print(result)
        if result != None:
            return redirect("/error?msg=信箱已經被註冊")
        cursor.execute("INSERT INTO `member` (name,email,password) VALUES (%s,%s,%s)",[name,email,password])
        connection_object.commit()
        return redirect("/")

# 登入路由
@tasks_blueprints.route("/signin",methods=["POST"])
def signin():
    email=request.form["email"]
    password=request.form["password"]
    if email=="" or password=="":
        return redirect("/error?msg=請輸入帳號、密碼")
    with connection_object.cursor(dictionary=True) as cursor:
        cursor.execute("SELECT `name`,`id` FROM `member` WHERE `email`=%s AND `password`=%s",[email,password])
        result=cursor.fetchone()
        if result==None:
            return redirect("/error?msg=帳號、或密碼輸入錯誤")
        session["name"]=result["name"]
        session["id"]=result["id"]
        return redirect("/member")

# 登出路由
@tasks_blueprints.route("/signout")
def signout():
    del session["name"]
    return redirect("/")
