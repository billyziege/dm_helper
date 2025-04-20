from flask import Blueprint, abort, redirect, request, url_for


acct_bp = Blueprint('accounts', __name__)


@acct_bp.route("/login")
def login():
    return '<p>This will be the login page.<p>'


@acct_bp.route("/create_account", methods=["GET", "POST"])
def create_account():
    if request.method == "POST":
        return redirect(url_for("index"))
    return '<p>This will be the account creation page.<p>'


@acct_bp.route("/logout")
def logout():
    abort(401)
    return '<p>This will be the logout page.<p>'
