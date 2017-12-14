import unittest
from visualize_results import read_csv_file


class ReadCsvTestCase(unittest.TestCase):
    #def testNotExistingFile(self):
    # self.assertRaises(FileNotFoundError, read_csv_file('./NotExistingPath/NotExisting.csv'))
    
    def testExtract2Columns(self):
        time, measurement_values = read_csv_file('./test_csv/test_2_column.csv')
        self.assertEqual(11, len(time))


if __name__ == '__main__':
    unittest.main()
