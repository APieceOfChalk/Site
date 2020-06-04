from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView

from flask_security import SQLAlchemySessionUserDatastore
from flask_security import Security
from flask_security import current_user

from flask import redirect, url_for, request

from flask_mail import Mail

from forms import ExtendedRegisterForm



app = Flask(__name__, static_folder='templates/images')
app.config.from_object(Configuration)
mail = Mail(app)


db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


### ADMIN ###
from models import *


class AdminMixin:
    def is_accessible(self):
        return current_user.has_role('admin')

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('security.login', next=request.url))


class AdminView(AdminMixin, ModelView):
    pass


class HomeAdminView(AdminMixin, AdminIndexView):
    pass


admin = Admin(app, 'SiteApp', url='/', index_view=HomeAdminView(name='Home'))
admin.add_view(ModelView(Post, db.session))

### FLASK-SECURITY ###
user_datastore = SQLAlchemySessionUserDatastore(db.session, User, Role)
security = Security(app, user_datastore, register_form=ExtendedRegisterForm)

admin.add_view(AdminView(User, db.session()))

admin.add_view(AdminView(Consultation, db.session()))