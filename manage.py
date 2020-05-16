import os

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app.main import create_app,db
from app.main.model import entry


app = create_app('dev')

app.app_context().push()

manager = Manager(app,db)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


@manager.command
def run():
    app.run()

if __name__ == '__main__':
    manager.run()