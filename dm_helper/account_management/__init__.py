import os

from dm_helper.account_management.account_manager import AccountManager
from flask_login import LoginManager
from dm_helper.account_management.routes import acct_bp

def set_up_account_management(app, config):
    app.secret_key = os.urandom(24)
    login = LoginManager(app)
    account_manager = AccountManager(config["database_files"]["account_management"])
    app.register_blueprint(acct_bp)
    return login, account_manager
