import math

height = int(input("Enter wall height (feet):\n"))
#print('{:.2f}'.format(height))

width = int(input("Enter wall width (feet):\n"))
#print('{:.2f}'.format(width))

wall_area = height * width
#print("Wall area:", '{:.2f}'.format(wall_area), "square feet")
print("Wall area:", wall_area, "square feet")

gal_of_paint = 350 # square ft

cans = wall_area / gal_of_paint

print("Paint needed:", '{:.2f}'.format(cans), "gallons")
print("Cans needed:", '{:.0f}'.format(cans), "can(s)\n")

costs = {
    "red": 35,
    "blue": 25,
    "green": 23
}
color = input("Choose a color to paint the wall:\n")
print("Cost of purchasing", color, "paint: $" + str(math.ceil(cans) * costs[color]))
