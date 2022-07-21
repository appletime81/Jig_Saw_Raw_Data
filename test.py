with open("test.txt", "r") as f:
    lines = f.readlines()

for line in lines:
    # 首先從index 71開使切割字串
    EMPTY_LINE_FLAG = True
    record_space_list = []
    item_list = []
    value_str = ""
    if len(line) == 1:
        EMPTY_LINE_FLAG = False
    start_index = 71
    tmp_line = line[start_index:]
    tmp_line_list = tmp_line.split("    ")
    if EMPTY_LINE_FLAG:
        if tmp_line_list[0][0] == " ":
            start_index += 1
            tmp_line = line[start_index:]
            tmp_line_list = tmp_line.split("    ")

    for i, tmp_str in enumerate(tmp_line_list):
        if tmp_str != " ":
            value_str += tmp_str
        if len(value_str) == 5:
            value_str = ""


