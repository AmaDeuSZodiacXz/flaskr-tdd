from flask_script import Manager
from flask_migrate import MigrateCommand
from project import app, db

# Initialize the manager
manager = Manager(app)

# Add migrate command to manager
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()
