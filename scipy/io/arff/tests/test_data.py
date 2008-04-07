#!/usr/bin/env python
"""Tests for parsing full arff files."""
import os

from scipy.testing import *

from scipy.io.arff.arffread import read_arff

data_path = os.path.join(os.path.dirname(__file__), 'data')

test4 = os.path.join(data_path, 'test4.arff')
expect4_data = [(0.1, 0.2, 0.3, 0.4, 'class1'), 
        (-0.1, -0.2, -0.3, -0.4, 'class2'), 
        (1, 2, 3, 4, 'class3')]


class DataTest(TestCase):
    def test1(self):
        """Parsing trivial file with nothing."""
        data, meta = read_arff(test4)
        for i in range(len(data)):
            for j in range(4):
                assert_array_almost_equal(expect4_data[i][j], data[i][j])

if __name__ == "__main__":
    nose.run(argv=['', __file__])
