import re
import pandas as pd

with open("2022-06-02_16;12;40.txt", "r") as f:
    content = f.readlines()

PRODUCTION_COUNT_FLAG = False
FORM_ALARM_ITEM_FLAG = False

for line in content:
    if re.search("Package\W+:\W+", line):
        print(re.search("Package\W+:\W+", line))
    if re.search("Lot No\W+:\W+", line):
        print(re.search("Lot No\W+:\W+", line))
        print(line.split(":")[1].strip())
    if re.search("Lot Started\W+:\W+", line):
        print(line.split(":")[1][1:])
    if re.search("PRODUCTION COUNT", line):
        print("PRODUCTION COUNT")

    # get PRODUCTION COUNT tanle
    if re.search("PRODUCTION COUNT", line):
        PRODUCTION_COUNT_FLAG = True

    if PRODUCTION_COUNT_FLAG and re.search("FORM", line):
        PRODUCTION_COUNT_FLAG = False

    # if PRODUCTION_COUNT_FLAG and re.search("ALIGN", line):
    #     print(line.split(" "))
    #     temp_items_list = list()
    #     for i in range(len(line.split(" "))):
    #         if line.split(" ")[i] != "" and line.split(" ")[i] != "ALIGN":
    #             temp_items_list.append(line.split(" ")[i])
    #     for item in temp_items_list:

    # set FORM ALARM ITEM flag if find string of 'FORM Alarm Item'
    if re.search("FORM Alarm Item", line):
        FORM_ALARM_ITEM_FLAG = True

    if FORM_ALARM_ITEM_FLAG and re.search("Light Alarm", line):
        print([num for num in line.split(" ") if num.replace(".", "").isdigit()][0])





# df_sheet_index = pd.read_excel("Golden_Output.xlsx", sheet_name="Table1")
# print(df_sheet_index.columns.tolist())
