import unittest
import datetime
from visualize_results import read_csv_file, get_readable_name


class ReadCsvTestCase(unittest.TestCase):
    # assert that an error is raised when the file doesn't exist
    def testNotExistingFile(self):
        with self.assertRaises(FileNotFoundError):
            read_csv_file('./NotExistingPath/NotExisting.csv')

    # define the data fixtures to compare with
    def get2ColComparisonData(self):
        time_test_2_columns = [datetime.date(1993, 12, 21), datetime.date(1993, 12, 22), datetime.date(1993, 12, 23),
                              datetime.date(1993, 12, 24), datetime.date(1993, 12, 25), datetime.date(1993, 12, 26),
                              datetime.date(1993, 12, 27), datetime.date(1993, 12, 28), datetime.date(1993, 12, 29),
                              datetime.date(1993, 12, 30), datetime.date(1993, 12, 31)]
        measurement_values_test_2_columns = [[2.495793, 2.963668, 2.426969, 2.243307, 3.397772, 2.978721, 2.39693,
                                             2.213019, 2.674208, 3.113357, 2.569548]]

        return time_test_2_columns, measurement_values_test_2_columns

    def get4ColComparisonData(self):
        time_test_4_colums = [
            datetime.date(1993, 12, 21), datetime.date(1993, 12, 22), datetime.date(1993, 12, 23),
            datetime.date(1993, 12, 24), datetime.date(1993, 12, 25), datetime.date(1993, 12, 26),
            datetime.date(1993, 12, 27), datetime.date(1993, 12, 28), datetime.date(1993, 12, 29),
            datetime.date(1993, 12, 30), datetime.date(1993, 12, 31)
        ]

        measurement_values_4_columns = [
            [2.495793, 2.963668, 2.426969, 2.243307, 3.397772, 2.978721, 2.39693,
             2.213019, 2.674208, 3.113357, 2.569548],
            [1.299943, 1.507736, 1.269481, 1.168486, 1.660334, 1.521089, 1.249496,
             1.153468, 1.381207, 1.590746, 1.350475],
            [0.546621, 0.618493, 0.535822, 0.496665, 0.664021, 0.618517, 0.527169,
             0.490445, 0.57043, 0.649322, 0.562607]
        ]

        return time_test_4_colums, measurement_values_4_columns

    def testExtract2Columns(self):
        time, measurement_values = read_csv_file('./test_csv/test_2_column.csv')
        # assert lengths of the result data
        self.assertEqual(11, len(time))
        self.assertEqual(11, len(measurement_values[0]))

        # compare data against fixtures
        timefixtures, datafixtures = self.get2ColComparisonData()

        self.assertListEqual(time, timefixtures)
        self.assertListEqual(measurement_values, datafixtures)

        # assert types of the result data
        self.assertTrue(type(time[0]) is datetime.date)
        self.assertTrue(type(measurement_values[0][0]) is float)

    def testExtract4Columns(self):
        time, measurement_values = read_csv_file('./test_csv/test_4_column.csv')
        # assert lengths of the result data
        self.assertEqual(11, len(time))
        self.assertEqual(11, len(measurement_values[0]))
        self.assertEqual(11, len(measurement_values[1]))
        self.assertEqual(11, len(measurement_values[2]))

        # compare data against fixtures
        timefixtures, datafixtures = self.get4ColComparisonData()

        self.assertListEqual(time, timefixtures)
        self.assertListEqual(measurement_values, datafixtures)

        # assert types of the result data
        self.assertTrue(type(time[0]) is datetime.date)
        self.assertTrue(type(measurement_values[0][0]) is float)
        self.assertTrue(type(measurement_values[1][0]) is float)
        self.assertTrue(type(measurement_values[2][0]) is float)

    def testLabelName(self):
        # check for readable variable names
        self.assertEqual(get_readable_name('geb_mit.ep'), 'Potential Evaporation [mm/d]')
        self.assertEqual(get_readable_name('not_defined_file'), 'not defined')
        self.assertEqual(get_readable_name(1), 'not defined')



# the test is only conducted if the file is not imported within an other modul, but executed directly in the shell
#
if __name__ == '__main__':
    unittest.main()
