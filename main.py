import json
import os
import re
import time
import pandas as pd

from glob import glob
from pprint import pprint

from openpyxl import load_workbook


def get_all_txtx_files(current_path):
    return glob(current_path + "/*.txt")


def table_1(content):  # content = lines
    global table_1_dict
    PRODUCTION_COUNT_FLAG = False
    FORM_ALARM_ITEM_FLAG = False

    for line in content:
        # get Package name
        if re.search("Package\W+:\W+", line):
            # print(line)
            table_1_dict["Package"].append(line.split(":")[1].split("\\")[1])

        # get Lot No
        if re.search("Lot No\W+:\W+", line):
            table_1_dict["Lot_No"].append(line.split(":")[1].strip())

        # get Lot Started
        if re.search("Lot Started\W+:\W+", line):
            table_1_dict["Lot_Started"].append(
                re.search(r"\d+/\d+/\d+ \d+:\d+:\d+", line).group()
            )

        # get Lot Finished
        if re.search("Lot Finished\W+:\W+", line):
            table_1_dict["Lot_Finished"].append(
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
            table_1_dict["Light_Alarm"].append(
                [num for num in line.split(" ") if num.replace(".", "").isdigit()][0]
            )

        if FORM_ALARM_ITEM_FLAG and re.search("Package Type", line):
            table_1_dict["Package_Type"].append(
                [num for num in line.split(" ") if num.replace(".", "").isdigit()][0]
            )

        if FORM_ALARM_ITEM_FLAG and re.search("Package Size", line):
            table_1_dict["Package_Size"].append(
                [num for num in line.split(" ") if num.replace(".", "").isdigit()][0]
            )

        if FORM_ALARM_ITEM_FLAG and re.search("Package Absence", line):
            table_1_dict["Package_Absence"].append(
                [num for num in line.split(" ") if num.replace(".", "").isdigit()][0]
            )

        if FORM_ALARM_ITEM_FLAG and re.search("Lead Count", line):
            table_1_dict["Lead_Count"].append(
                [num for num in line.split(" ") if num.replace(".", "").isdigit()][0]
            )

        if FORM_ALARM_ITEM_FLAG and re.search("Broken Lead", line):
            table_1_dict["Broken_Lead"].append(
                [num for num in line.split(" ") if num.replace(".", "").isdigit()][0]
            )

        if FORM_ALARM_ITEM_FLAG and re.search("Bent Lead", line):
            table_1_dict["Bent_Lead"].append(
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
            table_1_dict["Lead_Span"].append(
                [num for num in line.split(" ") if num.replace(".", "").isdigit()][0]
            )

        if FORM_ALARM_ITEM_FLAG and re.search("Terminal Dimension", line):
            table_1_dict["Terminal_Dimension"].append(
                [num for num in line.split(" ") if num.replace(".", "").isdigit()][0]
            )

        if FORM_ALARM_ITEM_FLAG and re.search("Chip Out", line):
            table_1_dict["Chip_Out"].append(
                [num for num in line.split(" ") if num.replace(".", "").isdigit()][0]
            )

        if FORM_ALARM_ITEM_FLAG and re.search("Mark Count", line):
            table_1_dict["Mark_Count"].append(
                [num for num in line.split(" ") if num.replace(".", "").isdigit()][0]
            )

        if FORM_ALARM_ITEM_FLAG and re.search("No Mark", line):
            table_1_dict["No_Mark"].append(
                [num for num in line.split(" ") if num.replace(".", "").isdigit()][0]
            )

        if FORM_ALARM_ITEM_FLAG and re.search("Mark Offset", line):
            table_1_dict["Mark_Offset"].append(
                [num for num in line.split(" ") if num.replace(".", "").isdigit()][0]
            )

        if FORM_ALARM_ITEM_FLAG and re.search("Wrong Char", line):
            table_1_dict["Wrong_Char"].append(
                [num for num in line.split(" ") if num.replace(".", "").isdigit()][0]
            )

        if FORM_ALARM_ITEM_FLAG and re.search("Broken Char", line):
            table_1_dict["Broken_Char"].append(
                [num for num in line.split(" ") if num.replace(".", "").isdigit()][0]
            )

        if FORM_ALARM_ITEM_FLAG and re.search("Residue Char", line):
            table_1_dict["Residue_Char"].append(
                [num for num in line.split(" ") if num.replace(".", "").isdigit()][0]
            )

        if FORM_ALARM_ITEM_FLAG and re.search("Missing Ref", line):
            table_1_dict["Missing_Ref"].append(
                [num for num in line.split(" ") if num.replace(".", "").isdigit()][0]
            )

        if FORM_ALARM_ITEM_FLAG and re.search("Mold Cont", line):
            table_1_dict["Mold_Cont"].append(
                [num for num in line.split(" ") if num.replace(".", "").isdigit()][0]
            )

        if FORM_ALARM_ITEM_FLAG and re.search("Shift Cut", line):
            table_1_dict["Shift_Cut"].append(
                [num for num in line.split(" ") if num.replace(".", "").isdigit()][0]
            )

            # close FORM ALARM ITEM FLAG
            FORM_ALARM_ITEM_FLAG = False


def table_2(content):  # content = lines
    global table_2_dict
    FORM_INSPECTION_RESULT_FLAG = False
    under_line_count = 0
    under_line = "----------"

    for line in content:
        item_list = []

        # find under line
        if re.search("FORM INSPECTION RESULT", line):
            FORM_INSPECTION_RESULT_FLAG = True
        if re.search(under_line, line) and FORM_INSPECTION_RESULT_FLAG:
            under_line_count += 1

        # get Package name
        if re.search("Package\W+:\W+", line):
            package_name = line.split(":")[1].split("\\")[1]

        # get Lot No
        if re.search("Lot No\W+:\W+", line):
            lot_number = line.split(":")[1].strip()

        # get Lot Started
        if re.search("Lot Started\W+:\W+", line):
            lot_started = re.search(r"\d+/\d+/\d+ \d+:\d+:\d+", line).group()

        # get Lot Finished
        if re.search("Lot Finished\W+:\W+", line):
            lot_finished = re.search(r"\d+/\d+/\d+ \d+:\d+:\d+", line).group()

        if (
            under_line_count == 2
            and FORM_INSPECTION_RESULT_FLAG
            and under_line not in line
        ):
            table_2_dict["Package"].append(package_name)
            table_2_dict["Lot_No"].append(lot_number)
            table_2_dict["Lot_Started"].append(lot_started)
            table_2_dict["Lot_Finished"].append(lot_finished)

            for i, item in enumerate(line.strip().split("  ")):
                if item != "":
                    item_list.append(item)
            for key, value in zip(TABLE_2_COL_NAMES, item_list):
                table_2_dict[key].append(value)


def detect_table_3_col_names(all_txt_files):
    col_names = []
    for file in all_txt_files:
        with open(file, "r") as f:
            content = f.readlines()

    for line in content:
        if line.startswith("    NO  Inspection"):
            col_names += [
                item.strip() for item in line.strip().split(" ") if item.strip() != ""
            ]

    return list(set(col_names))


def table_3(content, fileName):  # content = lines
    # declare variables
    global TABLE_3_COL_NAMES
    global table_3_dict
    global IF_SPLIT_SAVE_TABLE_3_FLAG

    tmp_col_names = None
    IF_SPLIT_SAVE_TABLE_3_FLAG = False
    TABLE_3_PART_DETECT_FLAG = False
    under_line = "----------"
    tmp_table_3_dict = {
        "Package": [],
        "Lot_No": [],
        "Lot_Started": [],
        "Lot_Finished": [],
    }

    # processing start
    print("----------------------------------")
    print(fileName)
    for line in content:
        if re.search("    NO  Inspection", line):
            tmp_col_names = [
                item.strip() for item in line.strip().split(" ") if item.strip() != ""
            ]
            TABLE_3_PART_DETECT_FLAG = True

        # get Package name
        if re.search("Package\W+:\W+", line):
            package_name = line.split(":")[1].split("\\")[1]

        # get Lot No
        if re.search("Lot No\W+:\W+", line):
            lot_number = line.split(":")[1].strip()

        # get Lot Started
        if re.search("Lot Started\W+:\W+", line):
            lot_started = re.search(r"\d+/\d+/\d+ \d+:\d+:\d+", line).group()

        # get Lot Finished
        if re.search("Lot Finished\W+:\W+", line):
            lot_finished = re.search(r"\d+/\d+/\d+ \d+:\d+:\d+", line).group()

        if (
            TABLE_3_PART_DETECT_FLAG
            and under_line not in line
            and "    NO  Inspection" not in line
            and len(line) != 1
        ):
            # generate item list
            item_list = line.strip().split(" ")
            item_list = [item for item in item_list if item != ""]
            if item_list:
                time_ = item_list.pop(2)
                item_list[1] += " " + time_

                if len(tmp_col_names) == len(item_list):
                    print(abs(len(tmp_col_names) - len(item_list)))
                    for key in TABLE_3_COL_NAMES[4:]:
                        if key in tmp_col_names:
                            table_3_dict[key].append(
                                item_list[tmp_col_names.index(key)]
                            )
                        else:
                            table_3_dict[key].append(0)
                    table_3_dict["Package"].append(package_name)
                    table_3_dict["Lot_No"].append(lot_number)
                    table_3_dict["Lot_Started"].append(lot_started)
                    table_3_dict["Lot_Finished"].append(lot_finished)
                elif len(tmp_col_names) < len(item_list):
                    print(abs(len(tmp_col_names) - len(item_list)))

                    IF_SPLIT_SAVE_TABLE_3_FLAG = True
                    if "Undefined" not in tmp_col_names:
                        tmp_col_names.append("Undefined")

                    # check dict if empty
                    if len(tmp_table_3_dict.keys()) == 4:
                        for col_name in tmp_col_names:
                            tmp_table_3_dict[col_name] = []

                    # insert data
                    for k, v in zip(tmp_col_names, item_list):
                        tmp_table_3_dict[k].append(v)

                    tmp_table_3_dict["Package"].append(package_name)
                    tmp_table_3_dict["Lot_No"].append(lot_number)
                    tmp_table_3_dict["Lot_Started"].append(lot_started)
                    tmp_table_3_dict["Lot_Finished"].append(lot_finished)
                elif len(tmp_col_names) > len(item_list):
                    print(abs(len(tmp_col_names) - len(item_list)))
                    IF_SPLIT_SAVE_TABLE_3_FLAG = True
                    item_list.append(0)

                    # check dict if empty
                    if len(tmp_table_3_dict.keys()) == 4:
                        for col_name in tmp_col_names:
                            tmp_table_3_dict[col_name] = []

                    # insert data
                    for k, v in zip(tmp_col_names, item_list):
                        tmp_table_3_dict[k].append(v)

                    tmp_table_3_dict["Package"].append(package_name)
                    tmp_table_3_dict["Lot_No"].append(lot_number)
                    tmp_table_3_dict["Lot_Started"].append(lot_started)
                    tmp_table_3_dict["Lot_Finished"].append(lot_finished)

    if IF_SPLIT_SAVE_TABLE_3_FLAG:
        # print("---------------------------------")
        # for k, v in tmp_table_3_dict.items():
        #     print(k, len(v))

        tmp_table_3_df = pd.DataFrame(tmp_table_3_dict)
        tmp_table_3_df.to_excel(f"{tmp_table_3_dict.get('Lot_No')[0]}.xlsx")


if __name__ == "__main__":
    start_time = time.time()
    txt_files = get_all_txtx_files(os.getcwd())
    file_name = "Golden_Output_Test.xlsx"
    table_3_col_names = detect_table_3_col_names(all_txt_files=txt_files)
    IF_SPLIT_SAVE_TABLE_3_FLAG = False

    TABLE_1_COL_NAMES = [
        "Package",
        "Lot_No",
        "Lot_Started",
        "Lot_Finished",
        "FORM_Total",
        "FORM_Good",
        "FORM_Rework",
        "FORM_Reject",
        "FORM_Yield",
        "Light_Alarm",
        "Package_Type",
        "Package_Size",
        "Package_Absence",
        "Lead_Count",
        "Broken_Lead",
        "Bent_Lead",
        "Intrusion",
        "Protrusion",
        "Lead_Span",
        "Terminal_Dimension",
        "Chip_Out",
        "Mark_Count",
        "No_Mark",
        "Mark_Offset",
        "Wrong_Char",
        "Broken_Char",
        "Residue_Char",
        "Missing_Ref",
        "Mold_Cont",
        "Shift_Cut",
    ]
    TABLE_2_COL_NAMES = [
        "Inspection_Item",
        "SPEC",
        "AVERAGE(+ERROR)",
        "MIN(+ERROR)",
        "MAX(+ERROR)",
        "MAX-MIN",
        "CPK",
    ]
    TABLE_3_COL_NAMES = ["Package", "Lot_No", "Lot_Started", "Lot_Finished"]
    table_3_sub_col_names = detect_table_3_col_names(all_txt_files=txt_files)
    TABLE_3_COL_NAMES += table_3_sub_col_names

    table_1_dict = dict([(col_name, list()) for col_name in TABLE_1_COL_NAMES])
    table_2_dict = dict(
        [
            (col_name, list())
            for col_name in ["Package", "Lot_No", "Lot_Started", "Lot_Finished"]
            + TABLE_2_COL_NAMES
        ]
    )
    table_3_dict = dict([(col_name, list()) for col_name in TABLE_3_COL_NAMES])

    for txt_file in txt_files:
        with open(txt_file, "r") as f:
            lines = f.readlines()
        # print("------------------------------------")
        # print(txt_file)
        table_1(lines)
        table_2(lines)
        # table_3(lines, txt_file)

    for k, v in table_1_dict.items():
        print(k, len(v))
    df_1 = pd.DataFrame(table_1_dict)
    df_2 = pd.DataFrame(table_2_dict)
    # df_3 = pd.DataFrame(table_3_dict)

    df_1.to_excel(
        "Golden_Output_Table_1.xlsx",
        sheet_name="Table1",
        index=False,
    )
    df_2.to_excel(
        "Golden_Output_Table_2.xlsx",
        sheet_name="Table2",
        index=False,
    )

    # remove all txt files
    for txt_file in txt_files:
        os.remove(txt_file)

    print("%s seconds" % (time.time() - start_time))
