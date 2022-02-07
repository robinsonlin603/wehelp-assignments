from flask import *
import mysql.connector
tasks_blueprints=Blueprint(
    "tasks",
    __name__,
    template_folder="templates",
)

# 錯誤路由
@tasks_blueprints.route("/error")
def error():
    message=request.args.get("msg","自訂的錯誤訊息")
    return render_template("/error.html",message=message)

# 註冊路由
@tasks_blueprints.route("/signup",methods=["POST"])
def signup():
    connection = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="goodtime123",
    database="member_system"
    )
    cursor = connection.cursor()
    name=request.form["name"]
    email=request.form["email"]
    password=request.form["password"]
    cursor.execute("SELECT `email` FROM `member` WHERE `email`=%s",[email])
    result=cursor.fetchone()
    if result != None:
        return redirect("/error?msg=信箱已經被註冊")
    cursor.execute("INSERT INTO `member` (name,email,password) VALUES (%s,%s,%s)",[name,email,password])
    connection.commit()
    return redirect("/")

# 登入路由
@tasks_blueprints.route("/signin",methods=["POST"])
def signin():
    connection = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="goodtime123",
    database="member_system"
    )
    cursor = connection.cursor(dictionary=True)
    email=request.form["email"]
    password=request.form["password"]
    if email=="" or password=="":
        return redirect("/error?msg=請輸入帳號、密碼")
    cursor.execute("SELECT `name` FROM `member` WHERE `email`=%s AND `password`=%s",[email,password])
    result=cursor.fetchone()
    if result==None:
        return redirect("/error?msg=帳號、或密碼輸入錯誤")
    session["name"]=result["name"]
    return redirect("/member")

# 登出路由
@tasks_blueprints.route("/signout")
def signout():
    del session["name"]
    return redirect("/")
