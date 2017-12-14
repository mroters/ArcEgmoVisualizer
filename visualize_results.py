import csv
import datetime


def read_csv_file(filepath):
    # import csv files to python, the filepaths are needed as input, for example
    # provided as command line parameters (dragged or copied to the shell).

    # preallocate variables
    time = []
    measurement_values = []

    # read csv file, '\t' means tab as delimiter not ','
    reader = csv.reader(open(filepath, "rt"), delimiter='\t')

    for row in reader:

        # '.strip()' deletes the empty space in the strange ArcEgmo file
        colA = row[0].strip()
        # delete the header of the ArcEgmo file
        if colA == 'time':
            for x in range(0, len(row) - 1):
                measurement_values.append([])

            continue
        # change the strange date string of the ArcEgmo file in a date format
        date = datetime.datetime.strptime(colA, '"%d.%m.%Y"').date()
        time.append(date)

        # change the second column from strings to floats
        colB = float(row[1].strip())
        measurement_values[0].append(colB)

        try:
            colC = float(row[2].strip())
            measurement_values[1].append(colC)
        except IndexError:
            continue

        try:
            colD = float(row[3].strip())
            measurement_values[2].append(colD)
        except IndexError:
            continue

    return time, measurement_values
