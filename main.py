import os
import re
import time
import json
import copy
import collections
import pandas as pd

from glob import glob


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


def table_3(content, file_name):  # content = lines
    # declare variables
    global TABLE_3_COL_NAMES
    global table_3_dict
    TABLE_3_PART_DETECT_FLAG = False
    under_line = "----------"

    # print("-----------------------------------------------------")
    # print(file_name)

    # process content
    for line_index, line in enumerate(content):
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

        if re.search("    NO  Inspection", line):
            TABLE_3_PART_DETECT_FLAG = True
            tmp_col_names = [
                item.strip() for item in line.strip().split(" ") if item.strip() != ""
            ]

            if "PkgSize(X/Y)" in tmp_col_names:
                pkg_size_x_index = tmp_col_names.index("PkgSize(X/Y)")
                pkg_size_y_index = tmp_col_names.index("PkgSize(X/Y)") + 1
                tmp_col_names.remove("PkgSize(X/Y)")
                tmp_col_names.insert(pkg_size_x_index, "PkgSize_X")
                tmp_col_names.insert(pkg_size_y_index, "PkgSize_Y")

        if (
            under_line not in line
            and "    NO  Inspection" not in line
            and TABLE_3_PART_DETECT_FLAG
            and len(line) > 1
        ):
            # if re.search("-\d+\.\d+", line):
            #     print(file_name)
            #     print(line_index + 1)
            #     print(line.strip())

            # 處理欄位名稱("NO", "Inspection", "DVNo", "XPos", "YPos", "Item")
            tmp_line = line[:72].strip()
            first_6_col_item_list = [x for x in tmp_line.split(" ") if x != ""]
            if len(first_6_col_item_list) == 8:
                first_6_col_item_list[1] += " " + first_6_col_item_list.pop(2)
                first_6_col_item_list[5] += " " + first_6_col_item_list.pop(6)
            if len(first_6_col_item_list) == 7:
                first_6_col_item_list[1] += " " + first_6_col_item_list.pop(2)
            for key, value in zip(
                ["NO", "Inspection", "DVNo", "XPos", "YPos", "Item"],
                first_6_col_item_list,
            ):
                table_3_dict[key].append(value)

            table_3_dict["Package"].append(package_name)
            table_3_dict["Lot_No"].append(lot_number)
            table_3_dict["Lot_Started"].append(lot_started)
            table_3_dict["Lot_Finished"].append(lot_finished)

            # 處理剩下的欄位
            tmp_line = line[72:]
            tmp_line_list = tmp_line.split("    ")
            final_tmp_list = []
            record_empty_str = []
            for i in range(len(tmp_line_list)):
                if tmp_line_list[i] == "":
                    record_empty_str.append("")
                if len(record_empty_str) % 2 == 0 and len(record_empty_str) != 0:
                    for _ in range(int(len(record_empty_str) / 2)):
                        final_tmp_list.append("0")
                    record_empty_str = []
                if tmp_line_list[i] != "":
                    final_tmp_list.append(tmp_line_list[i].strip())
            if len(final_tmp_list) < len(tmp_col_names[6:]):
                final_tmp_list.append("0")

            # 組成dict
            # if len(final_tmp_list) != len(tmp_col_names[6:]):
            #     print(f"line {line_index + 1} have problem")
            #     print(tmp_col_names[6:])
            #     print(final_tmp_list)

            for key, value in zip(tmp_col_names[6:], final_tmp_list):
                table_3_dict[key].append(value)
            for col_name in list(
                set(TABLE_3_COL_NAMES[4:])
                - set(tmp_col_names[6:])
                - {"NO", "Inspection", "DVNo", "XPos", "YPos", "Item"}
            ):
                table_3_dict[col_name].append("0")
            if len(final_tmp_list) != len(tmp_col_names[6:]) and re.search("-\d+\.\d+", line):
                print("-----------------------------------------------------")
                print(file_name)
                print("line {} have problem".format(line_index + 1))
                print(tmp_col_names[6:])
                print(tmp_line.split("    "))
                print(final_tmp_list)
                print(len(final_tmp_list), len(tmp_col_names[6:]))
            elif re.search("-\d+\.\d+", line):
                print("-----------------------------------------------------")
                print(file_name)
                print("line {} have problem".format(line_index + 1))
                print(tmp_col_names[6:])
                print(tmp_line.split("    "))
                print(final_tmp_list)
                print(len(final_tmp_list), len(tmp_col_names[6:]))




if __name__ == "__main__":
    start_time = time.time()
    txt_files = get_all_txtx_files(os.getcwd())
    file_name = "Golden_Output_Test.xlsx"
    no_value_dict = dict()
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
    # ------------------------- 組合Table 3的欄位名稱 -------------------------
    TABLE_3_COL_NAMES = ["Package", "Lot_No", "Lot_Started", "Lot_Finished"]
    table_3_sub_col_names = detect_table_3_col_names(all_txt_files=txt_files)
    # sort table_3_sub_col_names by first alphabet
    table_3_sub_col_names.sort(key=lambda x: x[0])

    TABLE_3_COL_NAMES.extend(table_3_sub_col_names)
    if "PkgSize(X/Y)" in TABLE_3_COL_NAMES:
        TABLE_3_COL_NAMES.remove("PkgSize(X/Y)")
        TABLE_3_COL_NAMES.extend(["PkgSize_X", "PkgSize_Y"])
    # -----------------------------------------------------------------------

    # ------------------------- 給定table1到table3的所有dictionary ------------
    table_1_dict = dict([(col_name, list()) for col_name in TABLE_1_COL_NAMES])
    table_2_dict = dict(
        [
            (col_name, list())
            for col_name in ["Package", "Lot_No", "Lot_Started", "Lot_Finished"]
            + TABLE_2_COL_NAMES
        ]
    )
    table_3_dict = dict([(col_name, list()) for col_name in TABLE_3_COL_NAMES])
    # -----------------------------------------------------------------------

    for txt_file in txt_files:
        with open(txt_file, "r") as f:
            lines = f.readlines()
        table_3(lines, txt_file)
        table_1(lines)
        table_2(lines)



    df_1 = pd.DataFrame(table_1_dict)
    df_2 = pd.DataFrame(table_2_dict)

    # 排序table_3_dict
    tmp_table_3_dict = copy.deepcopy(table_3_dict)
    first_part_table_3_dict = {}
    for col_name in TABLE_3_COL_NAMES[:4]:
        first_part_table_3_dict[col_name] = tmp_table_3_dict.pop(col_name)
    tmp_table_3_dict = collections.OrderedDict(
        sorted(tmp_table_3_dict.items(), key=lambda x: x[0])
    )
    table_3_dict = {**first_part_table_3_dict, **tmp_table_3_dict}
    for k, v in table_3_dict.items():
        print(k, len(v))

    # 如果Table3行數超過1048576，則分成多個Excel檔
    if len(table_3_dict["Package"]) > 1048576:
        part_numbers = (
            int(len(table_3_dict["Package"]) / 1048576)
            if not len(table_3_dict["Package"]) % 1048576
            else int(len(table_3_dict["Package"]) / 1048576) + 1
        )
        part_numbers_list = list(range(part_numbers))
        print(part_numbers_list)
    else:
        df_3 = pd.DataFrame(table_3_dict)
        df_3.to_excel(
            excel_writer=f"Golden_Output_Table_3_part.xlsx",
            sheet_name="Table3",
            index=False,
        )

    for part_number in part_numbers_list:
        table_3_dict_copy = copy.deepcopy(table_3_dict)
        for key, value in table_3_dict_copy.items():
            table_3_dict_copy[key] = value[
                part_number * 1048576 : (part_number + 1) * 1048576
            ]
        df_3 = pd.DataFrame(table_3_dict_copy)
        print(f"Processing part {part_number + 1}")
        df_3.to_excel(
            excel_writer=f"Golden_Output_Table_3_part{part_number + 1}.xlsx",
            sheet_name="Table3",
            index=False,
        )
        print(f"Processing part {part_number + 1} done !!!")

    df_1.to_excel(
        excel_writer="Golden_Output_Table_1.xlsx",
        sheet_name="Table1",
        index=False,
    )

    df_2.to_excel(
        excel_writer="Golden_Output_Table_2.xlsx",
        sheet_name="Table2",
        index=False,
    )

    # remove all txt files
    # for txt_file in txt_files:
    #     os.remove(txt_file)

    # save dict to json
    with open("no_value_dict.json", "w") as f:
        json.dump(no_value_dict, f, indent=4)

    print("%s seconds" % (time.time() - start_time))
