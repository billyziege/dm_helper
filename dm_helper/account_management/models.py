"""
Interface with the sqlalchemy orm for managing user account information.
"""
from typing import ClassType, ClassVar, Dict, List, Optional

from flask_bcrypt import Bcrypt
from flask_login import UserMixin
from sqlalchemy import ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from dm_helper.repr_base import ReprBase


bcrypt = Bcrypt()


class AccountBase(DeclarativeBase, ReprBase):
    """
    Base class to manage accounts needed for the GUI.
    """
    
    def describe(self) -> str:
        try:
            return self.description
        except AttributeError:
            return self.__repr__(self)

    
class User(AccountBase, UserMixin):
    """
    Table storing contact information for different users.
    """
    username_max: ClassVar[int] = 25
    full_name_max: ClassVar[int] = 25
    email_max: ClassVar[int] = 50
    # Interface for sqlalchemy 
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] =  mapped_column(String(username_max), nullable=False, unique=True)
    full_name: Mapped[Optional[str]]
    email: Mapped[str] = mapped_column(String(email_max), nullable=False)
    phone: Mapped[Optional[str]]
    password_hash: Mapped[str] = mapped_column(nullable=False)
    user_roles: Mapped[List["UserRole"]] = relationship(back_populates="user",
                                                        cascade="all, delete-orphan")
    # Unsure if this works.
    default_role: Mapped["UserRole"] = relationship(back_populates="user",
                                                    cascade="all, delete-orphan")
    # Interface for ReprBase
    _repr_list: ClassVar[str] = ["username", "full_name", "email", "phone"]
    # Keep track of current role.
    _current_role: ClassVar[ClassType] = None

    @property
    def password(self):
        raise AttributeError('Password not readable.')

    @password.setter
    def password(self, password: str):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
    
    def verify_password(self, password:str ) -> bool:
        return bcrypt.check_password_hash(self.password_hash, password)

    def current_role(self, role_str: str=None) -> ClassType:
        """
        Standard setter/getter.
        """
        if role_str != None:
            self._current_role = roles.get_role_dict()[role_str]
        return self._current_role


class UserRole(AccountBase):
    """
    Many to Many Table storing user and role information.
    """
    # Interface for sqlalchemy 
    __tablename__ = "role"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped["User"] = relationship(back_populates="user_roles")
    role_type: Mapped[str]
    # Interface for ReprBase
    _repr_list: ClassVar[str] = ["user_id", "role"]


#@login.user_loader
#def load_user(id):
#    return 0  accounts_db.session.get(User, int(id))
