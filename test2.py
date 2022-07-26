import re
from glob import glob
from pprint import pprint

under_line = "----------"

files = glob('*.txt')
for file in files:
    TABLE_3_PART_DETECT_FLAG = False
    with open(file, 'r') as f:
        lines = f.readlines()
    for i, line in enumerate(lines):
        if re.search("    NO  Inspection", line):
            TABLE_3_PART_DETECT_FLAG = True
        if (
                under_line not in line
                and "    NO  Inspection" not in line
                and TABLE_3_PART_DETECT_FLAG
                and len(line) > 1
        ):
            tmp_line = line[:72].strip()
            first_6_col_item_list = [x for x in tmp_line.split(" ") if x != ""]
            if len(first_6_col_item_list) == 8:
                first_6_col_item_list[1] += " " + first_6_col_item_list.pop(2)
                first_6_col_item_list[5] += " " + first_6_col_item_list.pop(6)
            if len(first_6_col_item_list) == 7:
                first_6_col_item_list[1] += " " + first_6_col_item_list.pop(2)

            if first_6_col_item_list[5] == "14":
                print(file)
                print(first_6_col_item_list[5])
                print(f"第{i + 1}行")
                pprint(first_6_col_item_list)
