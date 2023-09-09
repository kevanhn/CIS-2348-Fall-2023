# Kevin Nguyen 1928145

# (1) Output a menu of automotive services
# and the corresponding cost of each service. (2 pts)
print("Davy's auto shop services")
print("Oil change -- $35")
print("Tire rotation -- $19")
print("Car wash -- $7")
print("Car wax -- $12\n")

# (2) Prompt the user for two services from the menu. (2 pts)
first_service = input("Select first service:\n")
second_service = input("Select second service:\n")

# (3) Output an invoice for the services selected.
# Output the cost for each service and the total cost. (3 pts)
print()
print("Davy's auto shop invoice")
print()

if first_service == "Oil change":
    print(f'Service 1: {first_service}, $35')
elif first_service == "Tire rotation":
    print(f'Service 1: {first_service}, $19')
elif first_service == "Car wash":
    print(f'Service 1: {first_service}, $7')
elif first_service == "Car wax":
    print(f'Service 1: {first_service}, $12')
elif first_service == "-":
    print(f'Service 1: No service')

if second_service == "Oil change":
    print(f'Service 2: {second_service}, $35\n')
elif second_service == "Tire rotation":
    print(f'Service 2: {second_service}, $19\n')
elif second_service == "Car wash":
    print(f'Service 2: {second_service}, $7\n')
elif second_service == "Car wax":
    print(f'Service 2: {second_service}, $12\n')
elif second_service == "-":
    print(f'Service 2: No service\n')

# dictionary
prices = {"Oil change": 35, "Tire rotation": 19,"Car wash": 7, "Car wax": 12, "-": 0}

print(f'Total: ${prices[first_service]+ prices[second_service]}')

# (4) Extend the program to allow the user to enter a dash (-),
# which indicates no service. (3 pts)
