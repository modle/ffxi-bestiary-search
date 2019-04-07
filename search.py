import csv
import os
import sys

abs_path = os.path.dirname(os.path.abspath(__file__))
the_file = '{}/ffxi-db.csv'.format(abs_path)

LVL_DIFF = 10

NAME_INDEX = 1
FAMILY_INDEX = 2
TYPE_INDEX = 3
ZONE_INDEX = 5
MIN_LEVEL_INDEX = 10
MAX_LEVEL_INDEX = 11

def print_matches(matches):
    for entry in matches:
        print ("{}-{} {}: {}/{}, {}".format(
                entry[MIN_LEVEL_INDEX],
                entry[MAX_LEVEL_INDEX],
                entry[NAME_INDEX],
                entry[FAMILY_INDEX],
                entry[TYPE_INDEX],
                entry[ZONE_INDEX])
            )

while (True):
    # refresh the data every execution, because iterators
    with open(the_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        print ("enter type/family/name/zone and level")
        input_string = input ("--------------------------\n\n--> ")
        split_input = input_string.split(" ", 1)
        if len(split_input) < 2:
            print ("invalid entry\n")
            continue
        target = split_input[0]
        target_lvl = split_input[1]
        print ("checking for {} for lv {} +- {}...\n".format(target, target_lvl, LVL_DIFF))
        try:
            max_lvl = int(target_lvl) + LVL_DIFF
            min_lvl = int(target_lvl) - LVL_DIFF
        except:
            print ("invalid lvl, need int, got '{}'".format(target_lvl))
            continue

        matches = 0
        type_matches = []
        family_matches = []
        name_matches = []
        zone_matches = []

        for row in csv_reader:
            type_check = str(row[TYPE_INDEX]).lower()
            family_check = str(row[FAMILY_INDEX]).lower()
            name_check = str(row[NAME_INDEX]).lower()
            zone_check = str(row[ZONE_INDEX]).lower()
            min_check_lvl = -999
            max_check_lvl = 999
            try:
                min_check_lvl = int(row[MIN_LEVEL_INDEX])
            except:
                continue

            try:
                max_check_lvl = int(row[MAX_LEVEL_INDEX])
            except:
                continue

            if target in type_check and min_check_lvl > min_lvl and max_check_lvl < max_lvl:
                type_matches.append(row)

            if target in family_check and min_check_lvl > min_lvl and max_check_lvl < max_lvl:
                family_matches.append(row)

            if target in name_check and min_check_lvl > min_lvl and max_check_lvl < max_lvl:
                name_matches.append(row)

            if target in zone_check and min_check_lvl > min_lvl and max_check_lvl < max_lvl:
                zone_matches.append(row)

        print ("\n{} type matches:".format(len(type_matches)))
        print_matches(type_matches)
        print ("\n{} family matches:".format(len(family_matches)))
        print_matches(family_matches)
        print ("\n{} name matches:".format(len(name_matches)))
        print_matches(name_matches)
        print ("\n{} zone matches:".format(len(zone_matches)))
        print_matches(zone_matches)

