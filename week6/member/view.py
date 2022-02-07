from flask import *

member_blueprints=Blueprint(
    "member",
    __name__,
    template_folder="templates",
)

# 會員頁面
@member_blueprints.route("/member")
def member():
    if "name" in session:
        name=session["name"]
        if name=="":
            name="DEAT"
        return render_template("member.html",name=name)
    else:
        return redirect("/")
