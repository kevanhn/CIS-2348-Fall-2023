# FIXME (1): Finish reading other items into variables, then output the three ingredients
lemon_juice_cups = float(input('Enter amount of lemon juice (in cups):\n'))
water = float(input("Enter amount of water (in cups):\n"))
agave = float(input("Enter amount of agave nectar (in cups):\n"))
servings = float(input("How many servings does this make?\n\n"))
print("Lemonade ingredients - yields",f'{servings:.2f}',"servings")
print(f'{lemon_juice_cups:.2f}', "cup(s) lemon juice")
print(f'{water:.2f}', "cup(s) water")
print(f'{agave:.2f}', "cup(s) agave nectar\n")


# FIXME (2): Prompt user for desired number of servings. Convert and output the ingredients

desired_servings = float(input("How many servings would you like to make?\n\n"))
print("Lemonade ingredients - yields", f'{desired_servings:.2f}' ,"servings")

new_lemon = desired_servings / servings * 2
new_water = desired_servings / servings * 16
new_agave = desired_servings / servings * 2.5

print(f'{new_lemon:.2f}', "cup(s) lemon juice")
print(f'{new_water:.2f}', "cup(s) water")
print(f'{new_agave:.2f}', "cup(s) agave nectar\n")
# FIXME (3): Convert and output the ingredients from (2) to gallons

print("Lemonade ingredients - yields", f'{desired_servings:.2f}' ,"servings")
gal_lemon = new_lemon / 16
gal_water = new_water / 16
gal_agave = new_agave / 16

print(f'{gal_lemon:.2f}', "gallon(s) lemon juice")
print(f'{gal_water:.2f}', "gallon(s) water")
print(f'{gal_agave:.2f}', "gallon(s) agave nectar")