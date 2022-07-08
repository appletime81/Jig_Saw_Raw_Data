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
table_1_dict = dict([(col_name, list()) for col_name in TABLE_1_COL_NAMES])


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
            table_1_dict["Lot Started"].append(line.split(":")[1][1:])

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
            for key, value in zip(TABLE_1_COL_NAMES[5:9], temp_items_list):
                table_1_dict[key].append(value)

            # close PRODUCTION COUNT Flag
            PRODUCTION_COUNT_FLAG = False

        if FORM_ALARM_ITEM_FLAG and re.search("Light Alarm", line):
            table_1_dict["Light Alarm"] = [
                num for num in line.split(" ") if num.replace(".", "").isdigit()
            ][0]

        if FORM_ALARM_ITEM_FLAG and re.search("Package Type", line):
            table_1_dict["Package Type"] = [
                num for num in line.split(" ") if num.replace(".", "").isdigit()
            ][0]

        if FORM_ALARM_ITEM_FLAG and re.search("Package Size", line):
            table_1_dict["Package Size"] = [
                num for num in line.split(" ") if num.replace(".", "").isdigit()
            ][0]

        if FORM_ALARM_ITEM_FLAG and re.search("Package Absence", line):
            table_1_dict["Package Absence"] = [
                num for num in line.split(" ") if num.replace(".", "").isdigit()
            ][0]

        if FORM_ALARM_ITEM_FLAG and re.search("Lead Count", line):
            table_1_dict["Lead Count"] = [
                num for num in line.split(" ") if num.replace(".", "").isdigit()
            ][0]

        if FORM_ALARM_ITEM_FLAG and re.search("Broken Lead", line):
            table_1_dict["Broken Lead"] = [
                num for num in line.split(" ") if num.replace(".", "").isdigit()
            ][0]

        if FORM_ALARM_ITEM_FLAG and re.search("Bent Lead", line):
            table_1_dict["Bent Lead"] = [
                num for num in line.split(" ") if num.replace(".", "").isdigit()
            ][0]

        if FORM_ALARM_ITEM_FLAG and re.search("Intrusion", line):
            table_1_dict["Intrusion"].append([
                num for num in line.split(" ") if num.replace(".", "").isdigit()
            ][0])

        if FORM_ALARM_ITEM_FLAG and re.search("Protrusion", line):
            table_1_dict["Protrusion"].append([
                num for num in line.split(" ") if num.replace(".", "").isdigit()
            ][0])

        if FORM_ALARM_ITEM_FLAG and re.search("Lead Span", line):
            table_1_dict["Lead Span"].append([
                num for num in line.split(" ") if num.replace(".", "").isdigit()
            ][0])

        if FORM_ALARM_ITEM_FLAG and re.search("Terminal Dimension", line):
            table_1_dict["Terminal Dimension"].append([
                num for num in line.split(" ") if num.replace(".", "").isdigit()
            ][0])

        if FORM_ALARM_ITEM_FLAG and re.search("Chip Out", line):
            table_1_dict["Chip Out"].append([
                num for num in line.split(" ") if num.replace(".", "").isdigit()
            ][0])

        if FORM_ALARM_ITEM_FLAG and re.search("Mark Count", line):
            table_1_dict["Mark Count"].append([
                num for num in line.split(" ") if num.replace(".", "").isdigit()
            ][0])

        if FORM_ALARM_ITEM_FLAG and re.search("No Mark", line):
            table_1_dict["No Mark"].append([
                num for num in line.split(" ") if num.replace(".", "").isdigit()
            ][0])

        if FORM_ALARM_ITEM_FLAG and re.search("Mark Offset", line):
            table_1_dict["Mark Offset"].append([
                num for num in line.split(" ") if num.replace(".", "").isdigit()
            ][0])

        if FORM_ALARM_ITEM_FLAG and re.search("Wrong Char", line):
            table_1_dict["Wrong Char"].append([
                num for num in line.split(" ") if num.replace(".", "").isdigit()
            ][0])

        if FORM_ALARM_ITEM_FLAG and re.search("Broken Char", line):
            table_1_dict["Broken Char"].append([
                num for num in line.split(" ") if num.replace(".", "").isdigit()
            ][0])

        if FORM_ALARM_ITEM_FLAG and re.search("Residue Char", line):
            table_1_dict["Residue Char"].append([
                num for num in line.split(" ") if num.replace(".", "").isdigit()
            ][0])

        if FORM_ALARM_ITEM_FLAG and re.search("Missing Ref", line):
            table_1_dict["Missing Ref"].append([
                num for num in line.split(" ") if num.replace(".", "").isdigit()
            ][0])

        if FORM_ALARM_ITEM_FLAG and re.search("Mold Cont", line):
            table_1_dict["Mold Cont"].append([
                num for num in line.split(" ") if num.replace(".", "").isdigit()
            ][0])

        if FORM_ALARM_ITEM_FLAG and re.search("Shift Cut", line):
            table_1_dict["Shift Cut"].append([
                num for num in line.split(" ") if num.replace(".", "").isdigit()
            ][0])

            # close FORM ALARM ITEM FLAG
            FORM_ALARM_ITEM_FLAG = False


def table_2(content):  # content = lines
    pass


def table_3(content):  # content = lines
    pass


if __name__ == "__main__":
    txt_files = get_all_txtx_files(os.getcwd())
    for txt_file in txt_files:
        with open(txt_file, "r") as f:
            lines = f.readlines()
        table_1(lines)

    pprint(table_1_dict)
    writer = pd.ExcelWriter("Golden_Output_Copy.xlsx", engine="xlsxwriter")
    df = pd.DataFrame(table_1_dict)
    df.to_excel(writer, sheet_name="Sheet1", index=False)
    writer.save()
