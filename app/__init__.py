from flask import Flask
from config import Config
from.models import db
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

from . import models
from app.main.routes import main
from app.search.routes import search
from app.users.routes import users

app.register_blueprint(main)
app.register_blueprint(search)
app.register_blueprint(users)
