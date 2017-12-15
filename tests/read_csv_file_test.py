import unittest
import datetime
from visualize_results import read_csv_file


class ReadCsvTestCase(unittest.TestCase):
    # def testNotExistingFile(self):
    # self.assertRaises(FileNotFoundError, read_csv_file('./NotExistingPath/NotExisting.csv'))

    def testExtract2Columns(self):
        time, measurement_values = read_csv_file('./test_csv/test_2_column.csv')
        # assert lengths of the result data
        self.assertEqual(11, len(time))
        self.assertEqual(11, len(measurement_values[0]))
        # assert types of the result data
        self.assertTrue(type(time[0]) is datetime.date)
        self.assertTrue(type(measurement_values[0][0]) is float)

# the test is only conducted if the file is not imported within an other modul, but executed directly in the shell
#
if __name__ == '__main__':
    unittest.main()
