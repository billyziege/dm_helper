import re
import inspect
from typing import List, Dict, FunctionType, ClassType

from Flask import url_for

import roles 

def analyze_pattern(pattern: str) -> List[str]:
    """
    Finds all keywords within the pattern and returns them as a list.

    Args:
        pattern: String with keywords (to be replaced) inside squiggly brackets, {keyword}.
    
    Returns:
        matches: List of keywords.
    """
    matches = re.findall(r'\{\w+\}')
    return [m.replace("\{", "").replace("\}", "") for m in matches]



class SiteLink(object):
    """
    Keeps track of an endpoint attaching additional information.
    Import for building menus.
    """
    _anchor_template = '<a href="{url}">{name}</a>'
    _all_roles = roles.role_subclasses()
    _all_role_keywords = ["all", "all roles"]

    def __init__(self, name : str, endpoint : str, permitted_roles : List[ClassType] = []):
        self._name = name
        self._endpoint = endpoint
        self._name_keywords = set(analyze_pattern(name))
        self._permitted_roles = permitted_roles

    def name(self, **kwargs) -> str:
        """
        Replaces the keywords within the name with the provided keywords.

        Returns:
            name: The fomatted name.

        Raises:
            ValueError: If all keywords are not provided.
        """
        try:
            self._name.format(**kwargs)
        except KeyError:
            diff = self._name_keywords - set(kwargs.keys())
            err_msg = "Name {name} could not be built. ".format(name=self._name)
            err_msg += "Missing keyword(s): " + ", ".join(list(diff))
            raise ValueError(err_msg)
        
    def anchor(self, **kwargs) -> str:
        """
        Builds a url anchor string for the site link.

        Returns:
            An html anchor string.
        """
        return self._anchor_template.format(name=self.name(**kwargs), url=url_for(self._endpoint, **kwargs))

    def add_role(self, *role_list: List):
        for all_keyword in self._all_keywords:
            if all_keyword in role_list:
                self._roles = self._all_roles
                return
        for role in role_list:
            if role not in self._all_roles:
                raise ValueError("Role being registered is not recognized.")
        self._roles.extend(role_list)

    def validate_user(self, user: ClassType):
        """
        Checks the user's role against the roles registered with the Site Link.
        Returns whether the user's role is allowed in the site link.
        """
        return (user.current_role in self.user_roles)
            

class SiteMap(object):

    def __init__(self, blueprint=None):
        self._site_links = dict()
        self._current_blueprint = blueprint
        self._blueprints = []
        if blueprint:
            self._blueprints.append(blueprint)

    def register(self, name: str, roles: ListType[ClassType], func: FunctionType) -> FunctionType:
        """
        Decorator that adds a site link keyed and with the name to the site_links.
        """
        def decorated_func(*args):
            endpoint = func.__name__
            if self._current_blueprint:
                endpoint = blueprint.name + "/" + endpoint
            self._site_links[name] = SiteLink(name, endpoint)
            self._site_links[name].add_role(*roles)
            return func(*args)
        return decorated_func

    def blueprints(self):
        """
        Simple getter.
        """
        return self._blueprint

    def __items__(self):
        for name, url in self._site_links.items():
            yield name, url

    def __add__(self, other: ClassType[SiteMap]):
        """
        Overrides the '+' operator.
        """
        SiteMap(self._blueprint)
        for name, endpoint in other.items():
            self._site_links[name] = endpoint
        self._blueprints.extend(other._blueprints)
