with open("/home/marton/Projects/adventofcode/python/day2/data/input.txt","r") as file:
    lines = [line.rstrip() for line in file]

sum = 0

for line in lines:
    game_info, game_data = line.split(": ")
    draw_result_str = game_data.split("; ")
    color_count = {"red": 0, "green": 0, "blue": 0}
    for draw_str in draw_result_str:
        color_count_str = draw_str.split(", ")
        for string in color_count_str:
            count, color = string.split(" ")
            count = int(count)
            if count > color_count[color]:
                color_count[color] = count

    sum += color_count["red"] * color_count["green"] * color_count["blue"]

print(sum)