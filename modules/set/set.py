""" Module of set """
import ast
from accessify import implements
from modules.set.interface_set import ISet
from modules.tree.avl_tree import AVLTree

TYPES = {
    'int' : int,
    'str' : str,
    'float' : float,
    'bool' : bool,
    'list' : list,
    'dict' : dict,
    'set' : set,
}

@implements(ISet)
class Set():
    """ Class of set on avl tree """
    # pylint: disable=W0123
    # W0123 - Use of eval
    __tree = None
    __set_type = None

    def __init__(self, tree_type):
        """ Initialization """
        self.__tree = AVLTree()
        self.__set_type = tree_type
        if self.__set_type != 'int' and self.__set_type != 'float'\
        and self.__set_type != 'bool' and self.__set_type != 'str'\
        and self.__set_type != 'list' and self.__set_type != 'dict' and self.__set_type != 'set':
            raise SystemExit('TypeError : Wrong Type')

    def add(self, val):
        """ Add value in set """
        val = self._conversion(val)
        if isinstance(val, TYPES[self.__set_type]):
            self.__tree.insert(val)
        else:
            print("TypeError : Wrong Input")

    def clear(self):
        """ Delete all elements in set """
        del self.__tree
        self.__tree = AVLTree()
        print("Set is empty now")

    def remove(self, val):
        """ Remove element from set """
        val = self._conversion(val)
        if isinstance(val, TYPES[self.__set_type]):
            self.__tree.delete(val)
        else:
            print("TypeError : Wrong Input")

    def contains(self, val):
        """ Return true or node if contains, else False or None """
        val = self._conversion(val)
        if isinstance(val, TYPES[self.__set_type]):
            return self.__tree.search(val)
        else:
            print("TypeError : Wrong Input")

    def count(self):
        """ Get count of elements in set """
        return self.__tree.node_count

    def is_empty(self):
        """ Return true is not empty, else False """
        return True if self.__tree.node_count == 0 else False

    def _conversion(self, val):
        """ Convert value in needed type """
        if (self.__set_type == "str"):
            return val
        else:
            try:
                return ast.literal_eval(val)
            except ValueError:
                print("ValueError: Wrong input")
                return None
            