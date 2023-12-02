count_limits = {"red": 12, "green": 13, "blue": 14}

with open("/home/marton/Projects/adventofcode/python/day2/data/input.txt","r") as file:
    lines = [line.rstrip() for line in file]

sum = 0

for line in lines:
    game_info, game_data = line.split(": ")
    draw_result_str = game_data.split("; ")
    invalid_count = False
    for draw_str in draw_result_str:
        color_count_str = draw_str.split(", ")
        for string in color_count_str:
            count, color = string.split(" ")
            if int(count) > count_limits[color]:
                invalid_count = True
                break
        if invalid_count:
            break
    if not invalid_count:
        sum += int(game_info.split(" ")[1])

print(sum)