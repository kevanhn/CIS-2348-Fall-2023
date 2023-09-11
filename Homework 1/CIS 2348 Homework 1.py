# Kevin Nguyen
# 1928145

print("Birthday Calculator")
print("Current day")
current_month = int(input("Month: "))
current_day = int(input("Day: "))
current_year = int(input("Year: "))
print("Birthday")
birth_month = int(input("Month: "))
birth_day = int(input("Day: "))
birth_year = int(input("Year "))

if current_month == birth_month and current_day == birth_day:
    age = current_year - birth_year
    print(f'You are {age} years old.')
    print("Happy Birthday!")
elif current_month < birth_month or (current_month == birth_month and current_day < birth_day):
    age = current_year - birth_year - 1
    print(f'You are {age} years old.')
else:
    age = current_year - birth_year
    print(f'You are {age} years old.')

