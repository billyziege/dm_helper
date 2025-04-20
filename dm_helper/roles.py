""" 
Roles that are necessary for accessing different portions
of the graphic user interface.
"""
import inspect
from typing import Any, ClassType, Dict, List, Tuple
import sys

class Role(object):
    _role_type = "base"
    _description = "Base class that should not be used in practice."

    def __init__(self):
        _name = self.role_type + " role"

    def role(self):
        return role_type


class Admin(Role):
    _role_type = "admin"
    _description = "Role for managing users and roles."


class ContentCreator(Role):
    _role_type = "content-creator"
    _description = "Role for creating content within tables."


class DungeonMaster(Role):
    _role_type = "dungeon-master"
    _description = "Role for running a campaign.  Content creation is done within content creator role."


class Player(Role):
    _role_type = "player"
    _description = "Role for playing in a campaign.  Limitted access."


def is_subclass_of_role(obj: Any) -> bool:
  """
  Returns a boolean to the question "Is the object a subclass of Role?"
  """
  return inspect.isclass(obj) and issubclass(obj, Role)


def role_subclasses() -> List[ClassType]:
    """
    Gathers all of the subclasses of the Role class and returns them as a list.
    """
    return inspect.getmembers(sys.modules[__name__], is_subclass_of_role)


def roles_dict() -> Dict[str, ClassType]:
    """
    Creates a dictionary of role_types (key) to the Derived Class.
    """
    return dict([(cls.role_type, cls) for cls in role_subclasses()])
    

def roles_enum() -> List[Tuple(int, str)]:
    """
    Creates a "enum" that is a tuple pair consisting of a unique int and role_type.
    """
    return [(i, cls.role_type) for i, cls in enumerate(role_subclasses())]
