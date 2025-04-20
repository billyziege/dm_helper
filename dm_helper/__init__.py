import configparser

from flask import Flask

from dm_helper.account_management import set_up_account_management
from dm_helper.routes import base_bp

app = Flask(__name__)

config = configparser.ConfigParser()
config.read("dm_helper/configs/app_config.ini")

login, account_manager = set_up_account_management(app, config)
app.register_blueprint(base_bp)
