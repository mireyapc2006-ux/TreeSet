from Node import Node

class TreeSet:
    def __init__(self, value = None):
        if value != None:
            self.__root = Node(value)
            self.__size = 1
        else:
            self.__root = None
            self.__size = 0
    
    @property
    def root(self):
        return self.__root
    
    def size():
        return self.__size

