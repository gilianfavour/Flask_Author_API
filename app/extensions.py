# create a new database instance
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt


# new instance of flask Migrate
migrate = Migrate()# parameters are in the application facotory functions)

# Instance (db) as a variable
db = SQLAlchemy()

bcrypt = Bcrypt()
