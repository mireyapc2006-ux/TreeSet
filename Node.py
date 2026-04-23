class Node:
    def __init__(self, value = None, parent = None, left = None, right = None, color = None):
        self.__value = value
        self.__parent = parent
        self.__left = left
        self.__right = right
        self.__color = color # 0 = negro, 1 = rojo
    
    
    @property
    def parent(self):
        return self.__parent
 
    @property
    def left(self):
        return self.__left

    @property
    def right(self):
        return self.__right

    @property
    def value(self):
        return self.__value

    @property
    def color(self):
        return self.__color


    @parent.setter
    def parent(self, parent):
        self.__parent = parent
    
    @left.setter
    def left(self, left):
        self.__left = left
        
    @right.setter
    def right(self, right):
        self.__right = right
    
    @value.setter
    def value(self, value):
        self.__value = value
    
    @color.setter
    def color(self, color):
        self.__color = color
    

    def __str__(self):
        color = "red" if self.__color == 1 else "black"
        return f"({self.__value}, {color})"
    
    
