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
    
    def size(self):
        return self.__size
    
    def add(self, value):
        if self.contains(value):
            return False
        if self.__root is None:
            self.__root = Node(value)
            self.__first = self.__root
            self.__last = self.__root
        else:
           self._TreeSet__add_value(self.__root, value)
           self.__last = Node(value)
        
        self.__size += 1
        return True

    def __add_value(self, parent, value):
        if value < parent.value:
            if parent.left is None:
                parent.left = Node(value)
                return
            else:
                return self._TreeSet__add_value(parent.left, value)
        
        elif (value > parent.value):
            if parent.right is None:
                parent.right = Node(value)
                return
            else:
                return self._TreeSet__add_value(parent.right, value)
    
    def contains(self, value):
        if self.__size == 0:
            return False
        else:
            return self._TreeSet__search_value(self.__root, value)
    
    def __search_value(self, parent, value):
        if value == parent.value:
            return True
        elif value < parent.value:
            if parent.left is None:
                return False
            if parent.left.value == value:
                return True
            return self._TreeSet__search_value(parent.left, value)
        else:
            if parent.right is None:
                return False
            if parent.right.value == value:
                return True
            return self._TreeSet__search_value(parent.right, value)
        
    
    def is_empty(self):
        return self.__size == 0

    def clear(self):
        self.__root = None
        self.__size = 0
        self.__first = None
        self.__last = None

    @property
    def first(self):
        return self.__first
    
    def first(self):
        return self.__first
    
    @property
    def last(self):
        return self.__last
    
    def last(self):
        return self.__last
    
