import regex as re
input = open("input.txt", "r")
games = []
out = 0
# print(games)

for x in input:
    y = re.split('\W+', x[5:])
    games.append(y)



for x in games:
    print(x)
    index = x[0] # The game # we're currently on
    issues = False
    print(f'Index: {index}')
    for i,color in enumerate(x):
        if not any(char.isdigit() for char in color):
            qty = x[i-1]
            print(i,qty,color)
            
            if (color == 'red') and (int(qty) > 12):
                print('case1')
                issues = True
                
            elif (color == 'green') and (int(qty) > 13):
                print('case2')
                issues = True
                
            elif (color == 'blue') and (int(qty) > 14):
                print('case3')
                issues = True
    if issues == False:
        out = out + int(index)

print(f'Output: {out}')
