
from flask import Flask
from flask_sqlalchemy import SQLAlchemy     #SQLalchemy, for flask db functions
from flask_bcrypt import Bcrypt             #to hash passwords
from flask_login import LoginManager        #handles login requests
from flask_mail import Mail                 #to send reset email to users(in this case)
from app.config import Config



db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

mail = Mail()



def create_app(config_class = Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app (app)
    login_manager.init_app(app)
    mail.init_app(app)

    # Making necessary imports
    #imported later to deal with circular import
    from app.users.routes import users
    from app.posts.routes import posts
    from app.main.routes import main
    from app.errors.handlers import errors
    
    #Registering Blueprints
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app
