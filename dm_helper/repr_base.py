"""
A base class that can be used in multiple-inheritence to provide
a formulaic __repr__ method.
"""

class ReprBase(object):
    """
    A base class for having a nice repr function.
    """
    _repr_list = []

    def __repr__(self) -> str:
        output = self.__class__.__name__ + "("
        attr_fmt_list = []
        for attr_name in self._repr_list:
            attr_fmt_list.append(attr_name + "={" + attr_name + "}")
        output += ", ".join(attr_fmt_list) + ")"
        return output.format(**self.__dict__)


