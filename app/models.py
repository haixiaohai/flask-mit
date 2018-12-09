from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


@login.user_loader
def user_loader(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    __tablename__ = 'mit_users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), index=True)
    password_hash = db.Column(db.String(128))
    user_type = db.Column(db.String(120))

    def __repr__(self):
        return '<user %s>' % self.username

    def password_set(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Command(db.Model):
    __tablename__ = 'mit_commands'
    id = db.Column(db.Integer, primary_key=True)
    command = db.Column(db.String(120), index=True)
    exec_mode = db.Column(db.String(120))
    apply_to_device = db.Column(db.String(120))


class DeviceType(db.Model):
    __tablename__ = 'mit_devicetype'
    id = db.Column(db.Integer, primary_key=True)
    device_model = db.Column(db.String(120), index=True)
    device_class = db.Column(db.String(120), index=True)
