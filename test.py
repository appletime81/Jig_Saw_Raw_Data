import re
from pprint import pprint

with open("2022-06-25_21;28;21.txt", "r") as f:
    lines = f.readlines()

tmp_line_start_index = 72
tmp_line = "  10473  2022-06-25 22:13:57   17   10    15    Terminal Dimension      4.890    3.584    0.526             0.523    0.524    0.000    0.000    0.000    0.000    0.000    0.000    0.000    0.000    0.002    0.001    0.001    0.001    0.001    0.001    0.001   -0.003\n"
if tmp_line[tmp_line_start_index:].startswith("."):
    tmp_line_start_index = 71

print(tmp_line_start_index)
