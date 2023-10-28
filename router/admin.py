from flask import Blueprint, render_template, session, redirect, request
from flask_login import login_user, logout_user, current_user
from extension.utils import ip_ban

from flask_admin import AdminIndexView
from flask_admin.contrib.sqla import ModelView

from models import User


admin = Blueprint('admin_', __name__)


class Controller(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, **kwargs):
        # return redirect(url_for(''))
        pass

class AdminHome(AdminIndexView):
    def is_accessible(self):
        # return current_user.has_role('admin')
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return render_template('admin/login.html')
    

@admin.route('/login', methods=['GET','POST'])
def login():
    session.permanent = True
    name = request.form.get('name')
    if name is not None:
        user = User.query.filter_by(name=name).first()
        if user:
            login_user(user)
            return redirect('/admin')
    else:
        # ip = request.remote_addr
        return {":":"deny"}
    return render_template('admin/login.html')


@admin.route('/logout')
def logout():
    session.clear()
    logout_user()
    return "Logout access"