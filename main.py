import os
import re
import pandas as pd

from glob import glob
from pprint import pprint


TABLE_1_COL_NAMES = [
    "Package",
    "Lot No",
    "Lot Started",
    "Lot Finished",
    "FORM_Total",
    "FORM_Good",
    "FORM_Rework",
    "FORM_Reject",
    "FORM_Yield",
    "Light Alarm",
    "Package Type",
    "Package Size",
    "Package Absence",
    "Lead Count",
    "Broken Lead",
    "Bent Lead",
    "Intrusion",
    "Protrusion",
    "Lead Span",
    "Terminal Dimension",
    "Chip Out",
    "Mark Count",
    "No Mark",
    "Mark Offset",
    "Wrong Char",
    "Broken Char",
    "Residue Char",
    "Missing Ref",
    "Mold Cont",
    "Shift Cut",
]


def get_all_txtx_files(current_path):
    return glob(current_path + "/*.txt")


def table_1(content):  # content = lines
    table_1_dict = dict([(col_name, list()) for col_name in TABLE_1_COL_NAMES])
    PRODUCTION_COUNT_FLAG = False
    FORM_ALARM_ITEM = False
    for line in content:
        # get Package name
        if re.search("Package\W+:\W+", line):
            table_1_dict["Package"].append(line.split(":")[1].split("\\")[1])

        # get Lot No
        if re.search("Lot No\W+:\W+", line):
            table_1_dict["Lot No"].append(line.split(":")[1].strip())

        # get Lot Started
        if re.search("Lot Started\W+:\W+", line):
            table_1_dict["Lot Started"].append(line.split(":")[1][1:])

        # get PRODUCTION COUNT tanle
        if re.search("PRODUCTION COUNT", line):
            PRODUCTION_COUNT_FLAG = True

        if PRODUCTION_COUNT_FLAG and re.search("FORM", line):
            print(line.split(" "))
            temp_items_list = list()
            for i in range(len(line.split(" "))):
                if line.split(" ")[i] != "" and line.split(" ")[i] != "FORM":
                    temp_items_list.append(line.split(" ")[i])
            for key, value in zip(TABLE_1_COL_NAMES[5:9], temp_items_list):
                table_1_dict[key].append(value)

            # close PRODUCTION COUNT Flag
            PRODUCTION_COUNT_FLAG = False

        if
    pass


def table_2(content):  # content = lines
    pass


def table_3(content):  # content = lines
    pass


if __name__ == "__main__":
    txt_files = get_all_txtx_files(os.getcwd())
