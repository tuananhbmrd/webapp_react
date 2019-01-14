from flask_script import Manager
from flask_migrate import MigrateCommand

from app import create_app, db
from app.models import User, Role

manager = Manager(create_app)
manager.add_command('db', MigrateCommand)


@manager.command
def seed():
    find_or_create_roles("admin")
    find_or_create_roles("user")
    db.session.commit()


def find_or_create_roles(role_name):
    role = Role.query.filter_by(name=role_name).first()
    if not role:
        role = Role(name=role_name)
        db.session.add(role)

if __name__ == "__main__":
    manager.run()