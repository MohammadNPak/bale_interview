import unittest
from modified2 import binary_search

class TestBinarySearch(unittest.TestCase):

    def test_binary_search1(self):
        arr = [-3,-1,-1,0,0,0,0,1,1,2,2,2,2,3,3,3,]
        self.assertEqual(binary_search(arr,t=0),3)

    def test_binary_search2(self):
        arr = [-3,-1,-1,-1,-1,-1,1,1,2,2,2,2,3,3,3,]
        self.assertEqual(binary_search(arr,t=0),6)

    def test_binary_search3(self):
        arr = [-3,-1,-1,-1,-1,-1,1,1,2,2,2,2,3,3,3,]
        self.assertEqual(binary_search(arr,t=3),12)

    def test_binary_search4(self):
        arr = [-3,-1,-1,-1,-1,-1,1,1,2,2,2,2,3,3,3,]
        self.assertEqual(binary_search(arr,t=-2),1)

    def test_binary_search5(self):
        arr = [-3,-1,-1,-1,-1,-1,1,1,2,2,2,2,3,3,3,]
        self.assertEqual(binary_search(arr,t=-3),0)

    def test_binary_search6(self):
        arr = [-3,-1,-1,-1,-1,-1,1,1,2,2,2,2,3,3,3,4]
        self.assertEqual(binary_search(arr,t=4),15)

    def test_binary_search7(self):
        arr = [-3,-1,-1,-1,-1,-1,1,1,2,2,2,2,3,3,3,4]
        self.assertEqual(binary_search(arr,t=5),16)

if __name__=="__main__":
    unittest.main()
    