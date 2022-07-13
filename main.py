import os
import re
import time
import pandas as pd

from glob import glob
from pprint import pprint

from openpyxl import load_workbook

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
    "Inspection_Item",
    "SPEC",
    "AVERAGE(+ERROR)",
    "MIN(+ERROR)",
    "MAX(+ERROR)",
    "MAX-MIN",
    "CPK",
]

table_1_dict = dict([(col_name, list()) for col_name in TABLE_1_COL_NAMES])
table_2_dict = dict(
    [
        (col_name, list())
        for col_name in ["Package", "Lot No", "Lot Started", "Lot Finished"]
        + TABLE_2_COL_NAMES
    ]
)


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
            table_2_dict["Lot No"].append(lot_number)
            table_2_dict["Lot Started"].append(lot_started)
            table_2_dict["Lot Finished"].append(lot_finished)
            print("Package:", package_name)
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


def table_3(content):  # content = lines
    pass


if __name__ == "__main__":
    start_time = time.time()
    txt_files = get_all_txtx_files(os.getcwd())
    file_name = "Golden_Output拷貝.xlsx"
    table_3_col_names = detect_table_3_col_names(all_txt_files=txt_files)

    for txt_file in txt_files:
        # print(txt_file)
        with open(txt_file, "r") as f:
            lines = f.readlines()
        table_1(lines)
        table_2(lines)
    # pprint(table_2_dict)
    writer = pd.ExcelWriter(
        file_name, engine="openpyxl", mode="a", if_sheet_exists="overlay"
    )

    # detect if sheet and column name exist
    # case1: if exist
    if (
        "Table1" in writer.sheets
        and len(pd.read_excel(file_name, sheet_name="Table1").columns.tolist()) > 0
    ):
        # original data
        df_original_1 = pd.read_excel(file_name, sheet_name="Table1")
        df_original_2 = pd.read_excel(file_name, sheet_name="Table 2")
        df_1 = pd.DataFrame(table_1_dict)
        df_2 = pd.DataFrame(table_2_dict)
        # append new data
        df_1.to_excel(
            writer,
            header=None,
            sheet_name="Table1",
            index=False,
            startrow=len(df_original_1) + 1,
        )
        df_2.to_excel(
            writer,
            header=None,
            sheet_name="Table 2",
            index=False,
            startrow=len(df_original_2) + 1,
        )
        writer.save()
    else:
        # case2: if not exist
        df_1 = pd.DataFrame(table_1_dict)
        df_2 = pd.DataFrame(table_2_dict)
        df_1.to_excel(
            writer,
            header=None,
            sheet_name="Table1",
            index=False,
            startrow=1,
        )
        df_2.to_excel(
            writer,
            header=None,
            sheet_name="Table 2",
            index=False,
            startrow=1,
        )
        writer.save()
    print("%s seconds" % (time.time() - start_time))
