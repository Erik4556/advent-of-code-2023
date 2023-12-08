import regex as re
input = open("input.txt", "r")
output = 0

for x in input: 
    match_list = re.findall('[0-9]', x)
    calibration = match_list[0] + match_list[-1]
    output = output + int(calibration)

print(f'Total calibation sum is: {output}')