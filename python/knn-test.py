import unittest
import math
import knn

class TestKnn(unittest.TestCase):

    def test_euclidian_distance_1d(self):
        self.assertEqual(knn.euclidian_distance([0,0], [0,1], 2), 1)

    def test_euclidian_distance_2d(self):
        self.assertEqual(knn.euclidian_distance([0,0], [1,1], 2), math.sqrt(2.0))
