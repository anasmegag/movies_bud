from .model import Users
from . import db
from werkzeug.security import generate_password_hash, check_password_hash

def add_user(username, password):
    exist = Users.query.filter_by(username=username).first()
    if exist:
        return None, "User already exists"

    # Hashage du mot de passe avant stockage
    hashed_password = generate_password_hash(password)

    new_user = Users(username=username, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return new_user.id, "User added successfully"


def login_user(username, password):
    user = Users.query.filter_by(username=username).first()
    if not user:
        return None, "Invalid username or password"

    # Vérification du mot de passe avec le hash
    if not check_password_hash(user.password, password):
        return None, "Invalid username or password"

    return user.id, "Login successful"
