from sqlalchemy import select


from dm_helper.session_helper import start_session
from dm_helper.account_management.models import AccountBase, User, Role

class AccountManager(object):
    
    def __init__(self, db_file):
        self._db_file = db_file
        self._engine, self._session = start_session(self._db_file, AccountBase)
        stmt = select(User)
        if self._session.scalars(stmt).first() is None:
            self._empty = True
        else:
            self._empty = False 

    def empty(self):
        return self._empty

    def get_user(self, username):
        stmt = select(User).where(User.username.in_([username]))
        return self._session.scalars(stmt).one_or_none()
