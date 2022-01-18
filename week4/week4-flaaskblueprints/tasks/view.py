from flask import *
tasks_blueprints = Blueprint( 
    "tasks",
    __name__, 
    template_folder="templates" 
)

@tasks_blueprints.route("/signout")
def signout():
    del session["account"]
    return redirect("/")

@tasks_blueprints.route("/signin",methods=["POST"])
def signin():
    test_account="test"
    test_password="test"
    account=request.form["account"]
    password=request.form["password"]
    print(account)
    if account=="" or password=="":
        return redirect("/error?msg=請輸入帳號、密碼")
    elif account==test_account and password==test_password:
        session["account"]=account
        return redirect("/member")
    else:
        return redirect("/error?msg=帳號、或密碼輸入錯誤")