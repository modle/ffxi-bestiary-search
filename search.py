import csv
import os
import sys

abs_path = os.path.dirname(os.path.abspath(__file__))
the_file = '{}/ffxi-db.csv'.format(abs_path)
lvl_diff = 10

NAME_INDEX = 1
FAMILY_INDEX = 2
TYPE_INDEX = 3
ZONE_INDEX = 5
MIN_LEVEL_INDEX = 10
MAX_LEVEL_INDEX = 11

with open(the_file) as csv_file:
    while (True):
        csv_reader = csv.reader(csv_file, delimiter=',')
        print ("enter type and level")
        input_string = input ("--------------------------\n\n--> ")
        split_input = input_string.split(" ", 1)
        target = split_input[0]
        lvl = split_input[1]
        print ("checking for {} for lv {} +- {}...\n".format(target, lvl, lvl_diff))
        try:
            max = int(lvl) + lvl_diff
            min = int(lvl) - lvl_diff
        except:
            print ("invalid lvl, need int, got '{}'".format(lvl))
            continue

        matches = 0
        for row in csv_reader:
            check = str(row[FAMILY_INDEX]).lower()
            check_lvl = -99
            try:
                check_lvl = int(row[MIN_LEVEL_INDEX])
            except:
                continue

            if target in check and check_lvl > min and check_lvl < max:
                print ("{}-{} {}: {}/{}, {}".format(row[MIN_LEVEL_INDEX], row[MAX_LEVEL_INDEX], row[NAME_INDEX], row[FAMILY_INDEX], row[TYPE_INDEX], row[ZONE_INDEX]))
                matches += 1

        print ("\n{} matches\n".format(matches))

