from flask import request
from config import db, create_app
from models import User


from flask_admin import Admin
from flask_login import LoginManager

from router.main import main
from router.admin import admin, AdminHome, Controller


app = create_app()
login = LoginManager(app)


app.register_blueprint(main)
app.register_blueprint(admin)


request_count = {}  # Глобальная переменная для хранения количества запросов от каждого IP

@app.before_request
def limit_requests():
    ip = request.remote_addr
    if ip in request_count:
        request_count[ip] += 1
        print(request_count[ip])
        # if request_count[ip]
    else:
        request_count[ip] = 1
    print(request_count)
    

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)


panel = Admin(app, name="RedLine", url='/', index_view=AdminHome(name='Home'))
panel.add_view(Controller(User, db.session))


if __name__ == '__main__':
    app.run(debug=True)