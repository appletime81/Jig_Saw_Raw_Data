def detect_table_3_col_names(content):
    for line in content:
        if line.startswith("    NO  Inspection"):
            return [
                item.strip() for item in line.strip().split(" ") if item.strip() != ""
            ]


with open("2022-06-02_16;12;40.txt", "r") as f:
    lines = f.readlines()

from pprint import pprint
pprint(detect_table_3_col_names(lines))