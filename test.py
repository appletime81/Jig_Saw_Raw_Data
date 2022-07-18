from pprint import pprint


with open("2022-06-25_20;38;57.txt", "r") as f:
    lines = f.readlines()

# a_line = lines[20110][:72].strip()
# a_line_list = [x for x in a_line.split(" ") if x != ""]
# print(a_line_list)
#
# if len(a_line_list) == 8:
#     a_line_list[1] += " " + a_line_list.pop(2)
#     a_line_list[5] += " " + a_line_list.pop(6)
# if len(a_line_list) == 7:
#     a_line_list[1] += " " + a_line_list.pop(2)
# print(a_line_list)
# 20111
a_line = lines[20110][72:]
a_line_list = a_line.split("    ")
tmp_a_line_list = []
record_empty_str = []
for i in range(len(a_line_list)):
    if a_line_list[i] == "":
        record_empty_str.append("")
    if len(record_empty_str) % 2 == 0:
        for i in range(int(len(record_empty_str) / 2)):
            tmp_a_line_list.append("0")
        record_empty_str = []
    if a_line_list[i] != "":
        print(a_line_list[i])
        tmp_a_line_list.append(a_line_list[i])
print(a_line_list)
print(tmp_a_line_list)
print(len(tmp_a_line_list))
