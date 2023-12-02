import re

with open("/home/marton/Projects/adventofcode/python/day1/data/input.txt","r") as file:
    lines = [line.rstrip() for line in file]

sum = 0

for line in lines:
    str_nums = re.findall(r"\d",line)
    sum += int(str_nums[0] + str_nums[-1])

print(sum)