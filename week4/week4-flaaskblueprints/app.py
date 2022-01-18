from flask import *
from member.view import member_blueprints
from error.view import error_blueprints
from tasks.view import tasks_blueprints

app=Flask(
    __name__,
    static_folder="static",
    static_url_path="/",
)
app.secret_key="any string dont talk anyone"
app.register_blueprint(member_blueprints)
app.register_blueprint(error_blueprints)
app.register_blueprint(tasks_blueprints)

@app.route("/")
def home():
    return render_template("home.html")

app.run(port=3000)