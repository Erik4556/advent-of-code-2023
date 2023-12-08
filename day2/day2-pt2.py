import regex as re
input = open("input.txt", "r")
games = []
out = 0
# print(games)


# For each game, split every group of dice into individual list elements
# In this problem, the game deliniation is irrelevant, allowing us to split on any non-alphanumeric character set
for x in input:
    y = re.split('\W+', x[5:]) 
    games.append(y)



for x in games:
    print(x)
    rgb = [0,0,0] # 3 element list tracking the highest qty for red, green, and blue respectively
    rgb_key = {'red':0, 'green':1,'blue':2} # Index dictionary connecting a color string to the index in "rgb"

    for i,color in enumerate(x):
        if not any(char.isdigit() for char in color) and color != '':
            
            qty = int(x[i-1])
            print(i,qty,color, rgb[rgb_key[color]])
            # If a given qty on a given color is greater than the current top, update the list
            if qty > rgb[rgb_key[color]]:
                rgb[rgb_key[color]] = qty
                print(f'updated {color} to {qty}')
    power_set = rgb[0]*rgb[1]*rgb[2]
    print(f'Game {x[0]} results: power set of {power_set} from {rgb}')
    out = out + power_set
    
            

            
            


print(f'Output: {out}')
