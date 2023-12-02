import re

str_to_num_map = {"zero": '0',
                  "one": '1',
                  "two": '2',
                  "three": '3',
                  "four": '4',
                  "five": '5',
                  "six": '6',
                  "seven": '7',
                  "eight": '8',
                  "nine": '9'}

def str_to_numeric(string):
    return string if string.isnumeric() else str_to_num_map[string]

with open("/home/marton/Projects/adventofcode/python/day1/data/input.txt","r") as file:
    lines = [line.rstrip() for line in file]

sum = 0

for line in lines:
    str_nums = re.findall(r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))",line)
    sum += int(str_to_numeric(str_nums[0]) + str_to_numeric(str_nums[-1]))

print(sum)