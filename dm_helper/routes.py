from flask import Blueprint, abort, redirect, request, url_for


base_bp = Blueprint("base", __name__)


@base_bp.route("/")
@base_bp.route("/index")
def index():
    try:
        username = request.get_cookies().get("username")
        return f'<p>Logged in as {username}</p>'
    except Exception:
        pass
    return redirect(url_for('accounts.login'))
