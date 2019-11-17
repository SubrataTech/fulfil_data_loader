from decouple import config
from flask_sqlalchemy import SQLAlchemy as _BaseSQLAlchemy
from flask import Flask
from flask_migrate import Migrate

app = Flask(__name__)


class SQLAlchemy(_BaseSQLAlchemy):
    def apply_pool_defaults(self, app, options):
        super(SQLAlchemy, self).apply_pool_defaults(app, options)
        options["pool_pre_ping"] = True


def configure_app(app):
    app.config['ENV'] = config('ENV')
    app.config['DEBUG'] = config('DEBUG', cast=bool)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://{}:{}@{}:{}/{}'.format(
        config('MYSQL_USER'),
        config('MYSQL_PASSWORD'),
        config('MYSQL_HOST'),
        config('MYSQL_PORT'),
        config('MYSQL_DB')
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['SESSION_COOKIE_SECURE'] = True


configure_app(app)
db = SQLAlchemy(app)
db.init_app(app)
db.create_all()
db.session.commit()
migrate = Migrate(app, db)
