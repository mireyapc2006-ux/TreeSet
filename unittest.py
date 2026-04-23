import unittest
from Node import Node

class Tests(unittest.TestCase):
    
    # @classmethod
    # def setUpClass(cls):
    #     o1 = Node(5)
    
    def test_Node(self):
        o1 = Node(5)
        o1.color = 0
        self.assertEqual(o1.color, 0)

        o2 = Node(7)
        o1.right = o2
        o2.parent = o1
        o2.color = 1
        self.assertEqual(o1.right, o2)
        self.assertEqual(o2.parent, o1)
        self.assertEqual(o2.color, 1)
        
        o3 = Node(2)
        o1.left = o3
        o3.parent = o1
        o3.color = 1
        self.assertEqual(o1.left, o3)
        self.assertEqual(o3.parent, o1)
        self.assertEqual(o3.color, 1)
        
     
    @classmethod   
    def execute(cls):
        unittest.main()
