from config import db, create_app
from models import User

from flask_admin import Admin
from flask_login import LoginManager

from router.main import main
from router.admin import admin, AdminHome, Controller


app = create_app()
login = LoginManager(app)

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)


panel = Admin(app, name="RedLine", url='/', index_view=AdminHome(name='Home'))
panel.add_view(Controller(User, db.session))


app.register_blueprint(main)
app.register_blueprint(admin)


if __name__ == '__main__':
    app.run(debug=True)