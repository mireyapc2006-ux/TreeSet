from Node import Node

class TreeSet:
    def __init__(self, value = None):
        if value is not None:
            self.__root = Node(value)
            self.__size = 1
            self.__first = self.__root
            self.__last = self.__root
        else:
            self.__root = None
            self.__size = 0
            self.__first = None
            self.__last = None
    
    @property
    def root(self):
        return self.__root
    
    def size():
        return self.__size
    
    def add(self, value):
        if (self.__root is None):
            self.__root = Node(value)
        else:
            __add_value(self.__root, value)
        
        self.__size += 1

    def __add_value(self, parent, value):
        if (value < parent.value):
            if parent.left is None:
                parent.left = Node(value)
                return
            else:
                return __add_value(parent.left, value)
        
        elif (value > parent.value):
            if parent.right is None:
                parent.right = Node(value)
                return
            else:
                return __add_value(parent.right, value)
        
    
    def is_empty(self):
        return self.__size == 0

    def clear(self):
        self.__root = None
        self.__size = 0
        self.__first = None
        self.__last = None

    @property
    def first():
        return self.__first
    
    def first():
        return self.__first
    
    @property
    def last():
        return self.__last
    
    def last():
        return self.__last
    
    def __iter__(self):
        pass

