#!/usr/bin/env python
# visualize results from ArcEgmo exercise 1 from http://www.uebungen.arcegmo.de/html/_index.html

import csv  # gehört zur standard-bibliothek, muss nicht über pip installiert werden
import datetime  # gehört zur standard-bibliothek, muss nicht über pip installiert werden
import os
import sys
import matplotlib

matplotlib.use('TkAgg')  # mac specific backend problem
import matplotlib.pyplot as plt


def read_csv_file(filepath):
    # import csv files to python, the filepaths are needed as input, for example
    # provided as command line parameters (dragged or copied to the shell).

    # preallocate variables
    time = []
    measurement_values = []

    with open(filepath, "rt") as file_resource:
        # read csv file, '\t' means tab as delimiter not ','
        reader = csv.reader(file_resource, delimiter='\t')

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


def get_readable_name(filename):
    # return ArcEgmo file names in readable measurement variable names
    switcher = {
        'fgw_mit.qc': 'Total Runoff [mm/d]',
        'geb_mit.drain': 'Drainage Runoff [mm/d]',
        'geb_mit.ep': 'Potential Evaporation [mm/d]',
        'geb_mit.er': 'Actual Evaporation [mm/d]',
        'geb_mit.glo': 'Global Radiation',
        'geb_mit.gwn': 'Groundwater Recharge [mm/d]',
        'geb_mit.inter': 'Hypodermic Outflow [mm/d]',
        'geb_mit.mkr': 'Combined Sewer Outflow ',
        'geb_mit.pi': 'Precipitation [mm/d]',
        'geb_mit.ro': 'Surface Runoff [mm/d]',
        'geb_mit.tkr': 'Separation Sewer Outflow [mm/d]',
    }

    return switcher.get(filename, "not defined")


# 1. Ansatz (verworfen)
#
# listet die Files die in dem Ordner liegen in der Reihenfolge wie sie in dem Ordner erscheinen
# a = "./results"
# resultfiles = sorted(os.listdir(a))
#
# for measurement_variable in resultfiles:
#     if measurement_variable == '.DS_Store': # Speicherdatei, die der Mac automatisch anlegt
#         continue
#     filepath = './results/' + measurement_variable

# PROBLEM DABEI: es werden auch alle unsichtbaren Dateien, z.B. Systemdateien gelistet
# (wie die .DS_Store Datei). Diese kann man zwar jedesmal versuchen abzufangen,
# so wie ich hier mit der .DS_Store Datei, das ist aber ein große potentielle Fehlerquelle.
# Deshalb ist eine alternative Möglichkeit: Die Dateinamen als Argumente über
# die Shell/das Terminal zu übergeben, als sogenannte Kommandozeilenparameter.
# Diese werden als Liste an die Variable 'argv' im Modul 'sys' übergeben,
# wobei an erster Stelle (sys.argv[0]) der Name des Skriptes (Dateiname) steht.
# Die Argumente stehen ab der zweiten Stelle bis zum Ende der Liste (sys.argv[1:]):
filepaths = sys.argv[1:]
for filepath in filepaths:

    # import csv files with the read_csv_file function
    time, measurement_values = read_csv_file(filepath)

    # extract filename to save png's
    filename = os.path.basename(filepath)

    # loop through possible columns
    for x in range(0, len(measurement_values)):
        plt.plot(time, measurement_values[x])

    plt.xlabel('Time')
    ylabel = get_readable_name(filename)
    plt.ylabel(ylabel)
    plt.grid(linestyle='-.')

    # plt.show()
    plt.savefig('./result_plots/' + filename + '.png', format='png')
    # delete the last plot after saving, otherwise all graphs would be plottet in one figure
    plt.clf()
