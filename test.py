import re
import pandas as pd

with open("2022-06-02_16;12;40.txt", "r") as f:
    content = f.readlines()

for line in content:
    if re.search("Package\W+:\W+", line):
        print(re.search("Package\W+:\W+", line))
    if re.search("Lot No\W+:\W+", line):
        print(re.search("Lot No\W+:\W+", line))
        print(line.split(":")[1].strip())
    if re.search("Lot Started\W+:\W+", line):
        print(line.split(":")[1][1:])
# df_sheet_index = pd.read_excel("Golden_Output.xlsx", sheet_name="Table1")
# print(df_sheet_index.columns.tolist())
