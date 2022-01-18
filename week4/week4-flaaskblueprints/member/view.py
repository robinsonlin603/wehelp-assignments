from flask import *
member_blueprints = Blueprint( 
    "member",
    __name__, 
    template_folder="templates" 
)

@member_blueprints.route("/member")
def member():
    if "account" in session:
        return render_template("member.html")
    else:
        return redirect("/")