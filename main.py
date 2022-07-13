import os
import re
import time
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
TABLE_2_COL_NAMES = [
    "SPEC",
    "AVERAGE(+ERROR)",
    "MIN(+ERROR)",
    "MAX-MIN",
    "CPK"
]
table_1_dict = dict([(col_name, list()) for col_name in TABLE_1_COL_NAMES])
table_2_dict = dict([(col_name, list()) for col_name in TABLE_2_COL_NAMES])


def get_all_txtx_files(current_path):
    return glob(current_path + "/*.txt")


def table_1(content):  # content = lines
    global table_1_dict
    PRODUCTION_COUNT_FLAG = False
    FORM_ALARM_ITEM_FLAG = False

    for line in content:
        # get Package name
        if re.search("Package\W+:\W+", line):
            table_1_dict["Package"].append(line.split(":")[1].split("\\")[1])

        # get Lot No
        if re.search("Lot No\W+:\W+", line):
            table_1_dict["Lot No"].append(line.split(":")[1].strip())

        # get Lot Started
        if re.search("Lot Started\W+:\W+", line):
            table_1_dict["Lot Started"].append(
                re.search(r"\d+/\d+/\d+ \d+:\d+:\d+", line).group()
            )

        # get Lot Finished
        if re.search("Lot Finished\W+:\W+", line):
            table_1_dict["Lot Finished"].append(
                re.search(r"\d+/\d+/\d+ \d+:\d+:\d+", line).group()
            )

        # set PRODUCTION COUNT flag if find string of 'PRODUCTION COUNT'
        if re.search("PRODUCTION COUNT", line):
            PRODUCTION_COUNT_FLAG = True

        # set FORM ALARM ITEM flag if find string of 'FORM Alarm Item'
        if re.search("FORM Alarm Item", line):
            FORM_ALARM_ITEM_FLAG = True

        if PRODUCTION_COUNT_FLAG and re.search("FORM", line):
            temp_items_list = list()
            for i in range(len(line.split(" "))):
                if line.split(" ")[i] != "" and line.split(" ")[i] != "FORM":
                    temp_items_list.append(line.split(" ")[i])
            for key, value in zip(TABLE_1_COL_NAMES[4:9], temp_items_list):
                table_1_dict[key].append(value)

            # close PRODUCTION COUNT Flag
            PRODUCTION_COUNT_FLAG = False

        if FORM_ALARM_ITEM_FLAG and re.search("Light Alarm", line):
            table_1_dict["Light Alarm"].append(
                [num for num in line.split(" ") if num.replace(".", "").isdigit()][0]
            )

        if FORM_ALARM_ITEM_FLAG and re.search("Package Type", line):
            table_1_dict["Package Type"].append(
                [num for num in line.split(" ") if num.replace(".", "").isdigit()][0]
            )

        if FORM_ALARM_ITEM_FLAG and re.search("Package Size", line):
            table_1_dict["Package Size"].append(
                [num for num in line.split(" ") if num.replace(".", "").isdigit()][0]
            )

        if FORM_ALARM_ITEM_FLAG and re.search("Package Absence", line):
            table_1_dict["Package Absence"].append(
                [num for num in line.split(" ") if num.replace(".", "").isdigit()][0]
            )

        if FORM_ALARM_ITEM_FLAG and re.search("Lead Count", line):
            table_1_dict["Lead Count"].append(
                [num for num in line.split(" ") if num.replace(".", "").isdigit()][0]
            )

        if FORM_ALARM_ITEM_FLAG and re.search("Broken Lead", line):
            table_1_dict["Broken Lead"].append(
                [num for num in line.split(" ") if num.replace(".", "").isdigit()][0]
            )

        if FORM_ALARM_ITEM_FLAG and re.search("Bent Lead", line):
            table_1_dict["Bent Lead"].append(
                [num for num in line.split(" ") if num.replace(".", "").isdigit()][0]
            )

        if FORM_ALARM_ITEM_FLAG and re.search("Intrusion", line):
            table_1_dict["Intrusion"].append(
                [num for num in line.split(" ") if num.replace(".", "").isdigit()][0]
            )

        if FORM_ALARM_ITEM_FLAG and re.search("Protrusion", line):
            table_1_dict["Protrusion"].append(
                [num for num in line.split(" ") if num.replace(".", "").isdigit()][0]
            )

        if FORM_ALARM_ITEM_FLAG and re.search("Lead Span", line):
            table_1_dict["Lead Span"].append(
                [num for num in line.split(" ") if num.replace(".", "").isdigit()][0]
            )

        if FORM_ALARM_ITEM_FLAG and re.search("Terminal Dimension", line):
            table_1_dict["Terminal Dimension"].append(
                [num for num in line.split(" ") if num.replace(".", "").isdigit()][0]
            )

        if FORM_ALARM_ITEM_FLAG and re.search("Chip Out", line):
            table_1_dict["Chip Out"].append(
                [num for num in line.split(" ") if num.replace(".", "").isdigit()][0]
            )

        if FORM_ALARM_ITEM_FLAG and re.search("Mark Count", line):
            table_1_dict["Mark Count"].append(
                [num for num in line.split(" ") if num.replace(".", "").isdigit()][0]
            )

        if FORM_ALARM_ITEM_FLAG and re.search("No Mark", line):
            table_1_dict["No Mark"].append(
                [num for num in line.split(" ") if num.replace(".", "").isdigit()][0]
            )

        if FORM_ALARM_ITEM_FLAG and re.search("Mark Offset", line):
            table_1_dict["Mark Offset"].append(
                [num for num in line.split(" ") if num.replace(".", "").isdigit()][0]
            )

        if FORM_ALARM_ITEM_FLAG and re.search("Wrong Char", line):
            table_1_dict["Wrong Char"].append(
                [num for num in line.split(" ") if num.replace(".", "").isdigit()][0]
            )

        if FORM_ALARM_ITEM_FLAG and re.search("Broken Char", line):
            table_1_dict["Broken Char"].append(
                [num for num in line.split(" ") if num.replace(".", "").isdigit()][0]
            )

        if FORM_ALARM_ITEM_FLAG and re.search("Residue Char", line):
            table_1_dict["Residue Char"].append(
                [num for num in line.split(" ") if num.replace(".", "").isdigit()][0]
            )

        if FORM_ALARM_ITEM_FLAG and re.search("Missing Ref", line):
            table_1_dict["Missing Ref"].append(
                [num for num in line.split(" ") if num.replace(".", "").isdigit()][0]
            )

        if FORM_ALARM_ITEM_FLAG and re.search("Mold Cont", line):
            table_1_dict["Mold Cont"].append(
                [num for num in line.split(" ") if num.replace(".", "").isdigit()][0]
            )

        if FORM_ALARM_ITEM_FLAG and re.search("Shift Cut", line):
            table_1_dict["Shift Cut"].append(
                [num for num in line.split(" ") if num.replace(".", "").isdigit()][0]
            )

            # close FORM ALARM ITEM FLAG
            FORM_ALARM_ITEM_FLAG = False


def table_2(content):  # content = lines
    global table_2_dict
    FORM_INSPECTION_RESULT_FLAG = False
    under_line_count = 0
    under_line = "----------"

    table_2_dict["Package"] = []
    table_2_dict["Lot Num"] = []
    table_2_dict["Lot Started"] = []
    table_2_dict["Lot Finished"] = []

    for line in content:
        if re.search("Package", line):
            table_2_dict["Package"].append(
                [num for num in line.split(" ") if num.replace(".", "").isdigit()][0]
            )

        if re.search("Lot Num", line):
            table_2_dict["Lot Num"].append(
                [num for num in line.split(" ") if num.replace(".", "").isdigit()][0]
            )

        if re.search("Lot Started", line):
            table_2_dict["Lot Started"].append(
                [num for num in line.split(" ") if num.replace(".", "").isdigit()][0]
            )

        if re.search("Lot Finished", line):
            table_2_dict["Lot Finished"].append(
                [num for num in line.split(" ") if num.replace(".", "").isdigit()][0]
            )

        # find under line
        if re.search(under_line, line):
            under_line_count += 1
        if under_line_count == 2:
            FORM_INSPECTION_RESULT_FLAG = True
            under_line_count = 0





def table_3(content):  # content = lines
    pass


if __name__ == "__main__":
    start_time = time.time()
    txt_files = get_all_txtx_files(os.getcwd())
    for txt_file in txt_files:
        # print(txt_file)
        with open(txt_file, "r") as f:
            lines = f.readlines()
        table_1(lines)

    # Table 1
    table_1_original_data = pd.read_excel("Golden_Output_Copy.xlsx", sheet_name="Table1")
    df_1 = pd.DataFrame(table_1_dict)
    # append to original data
    table_1_final_data = table_1_original_data.append(df_1)
    table_1_final_data.to_excel("Golden_Output_Copy.xlsx", sheet_name="Table1")

    # Table 2


    print("--- %s seconds ---" % (time.time() - start_time))
