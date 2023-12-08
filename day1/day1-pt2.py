import regex as re
input = open("input.txt", "r")
output = 0

# input = [
#     'two1nine',
# 'eightwothree',
# 'abcone2threexyz',
# 'xtwone3four',
# '4nineeightseven2',
# 'zoneight234',
# '7pqrstsixteen'
# ]


for x in input: 

    x = re.sub('one', 'one1one', x)
    x = re.sub('two', 'two2two', x)
    x = re.sub('three', 'three3three', x)
    x = re.sub('four', 'four4four', x)
    x = re.sub('five', 'five5five', x)
    x = re.sub('six', 'six6six', x)
    x = re.sub('seven', 'seven7seven', x)
    x = re.sub('eight', 'eight8eight', x)
    x = re.sub('nine', 'nine9nine', x)

    print(x)
    match_list = re.findall('[0-9]', x)
    print(match_list)
    calibration = match_list[0] + match_list[-1]
    output = output + int(calibration)

print(f'Total calibation sum is: {output}')