from asyncio.windows_events import NULL
from flask import *
app=Flask(
    __name__,
    static_folder="templates",
    static_url_path="/",
)
app.secret_key="any string dont talk anyone"

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/member")
def member():
    if "account" in session:
        return render_template("member.html")
    else:
        return redirect("/")

@app.route("/error")
def error():
    message=request.args.get("msg","自訂的錯誤訊息")
    return render_template("error.html",message=message)

@app.route("/signin",methods=["POST"])
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

@app.route("/signout")
def signout():
    del session["account"]
    return redirect("/")

app.run(port=3000)