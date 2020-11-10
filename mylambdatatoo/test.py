import os
import unittest

from glob import glob

from ds_utilities import MyReadyFrame
from test_frames import DF_TEST_2


class TestMyReadyFrame(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.test_data = MyReadyFrame(DF_TEST_2, True, True, True, True)
        self.test_data_2 = MyReadyFrame(DF_TEST_2, False, False, False, False)
        self.test_data_3 = MyReadyFrame(DF_TEST_2, False, True, True, False)

    def tearDown(self):
        for f in glob("saved_test_data_*"):
            os.remove(f)

    def test_repr(self):
        self.assertEqual(repr(self.test_data),
        """The dataframe to be examined/cleaned has shape (6, 4).""")

    def test_str(self):
        self.assertEqual(str(self.test_data_2), """Frame shape: (6, 4). Null types: 0.""")

    def test_null_counts_false(self):
        self.assertEqual(MyReadyFrame.null_counts(self.test_data_2), "No count of null values requested. Please change an attribute to True.")

    def test_null_counts_true(self):
        self.assertEqual(MyReadyFrame.null_counts(self.test_data).shape[0], 4)
        self.assertEqual(MyReadyFrame.null_counts(self.test_data_3).shape[0], 2)

if __name__ == '__main__':
    unittest.main()
