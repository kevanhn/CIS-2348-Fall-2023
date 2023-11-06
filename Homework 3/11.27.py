# Kevin Nguyen 1928145

roster = {}

for i in range(5):
    jersey_number = int(input(f"Enter player {i+1}'s jersey number:\n"))
    rating = int(input(f"Enter player {i+1}'s rating:\n"))
    print()
    roster[jersey_number] = rating

sorted_roster = dict(sorted(roster.items()))
print("ROSTER")
for jersey, rating in sorted_roster.items():
    print(f"Jersey number: {jersey}, Rating: {rating}")

while True:
    print("\nMENU")
    print("a - Add player")
    print("d - Remove player")
    print("u - Update player rating")
    print("r - Output players above a rating")
    print("o - Output roster")
    print("q - Quit\n")
    option = input("Choose an option:\n")

    if option == 'a':
        jersey_number = int(input("Enter a new player's jersey number: "))
        rating = int(input("Enter the player's rating: "))
        roster[jersey_number] = rating
    elif option == 'd':  # Remove player
        jersey_number = int(input("Enter a jersey number: "))
        if jersey_number in roster:
            del roster[jersey_number]
    elif option == 'u':
        jersey_number = int(input("Enter a jersey number: "))
        if jersey_number in roster:
            new_rating = int(input("Enter a new rating for the player: "))
            roster[jersey_number] = new_rating
    elif option == 'r':
        rating_threshold = int(input("Enter a rating: "))
        print("\nABOVE", rating_threshold)
        for jersey, rating in sorted_roster.items():
            if rating > rating_threshold:
                print(f"Jersey number: {jersey}, Rating: {rating}")
    elif option == 'o':
        print("\nROSTER")
        for jersey, rating in sorted_roster.items():
            print(f"Jersey number: {jersey}, Rating: {rating}")
    elif option == 'q':  # Quit
        break
