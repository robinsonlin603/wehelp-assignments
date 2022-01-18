from flask import *
error_blueprints = Blueprint( 
    "error",
    __name__, 
    template_folder="templates" 
)

@error_blueprints.route("/error")
def error():
    message=request.args.get("msg","自訂的錯誤訊息")
    return render_template("error.html",message=message)