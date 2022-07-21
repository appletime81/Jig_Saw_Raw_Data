with open("test.txt", "r") as f:
    lines = f.readlines()

for line in lines:
    # 首先從index 71開使切割字串
    EMPTY_LINE_FLAG = True
    START_DETECT_SPACE_FLAG = False
    record_space_list = []
    item_list = []
    start_index = 71
    value_str = ""
    if len(line) == 1:
        EMPTY_LINE_FLAG = False
    tmp_line = line[start_index:]
    tmp_line_list = tmp_line.split("    ")
    if EMPTY_LINE_FLAG:
        if tmp_line_list[0][0] == " ":
            start_index += 1
            tmp_line = line[start_index:]
            tmp_line_list = tmp_line.split("    ")
    print(tmp_line.strip())
    for i, tmp_str in enumerate(tmp_line):
        if tmp_str != " ":
            value_str += tmp_str
            START_DETECT_SPACE_FLAG = False
        if (len(value_str) == 5 and "-" not in value_str) or (
            len(value_str) == 6 and "-" in value_str
        ):
            # print("I am here")
            item_list.append(value_str)
            # 重置value_str，START_DETECT_SPACE_FLAG為True
            value_str = ""
            START_DETECT_SPACE_FLAG = True
        if START_DETECT_SPACE_FLAG and tmp_str == " ":
            record_space_list.append(tmp_str)

        # 計算值與值之間有幾個空格，來判斷有幾個缺失值
        if not START_DETECT_SPACE_FLAG and i > 0:
            no_value_count = int(len(record_space_list) / 9)
            for _ in range(no_value_count):
                item_list.append("0")

            # 重置record_space_list
            record_space_list = []
    print(item_list, len(item_list))

