from datetime import date


def format_date(date_str):
    # dict to map month names to their number
    months = {
        "January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6,
        "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12}

    # get rid of white spaces, split into parts
    parts = date_str.split()

    # make sure string has 3 parts: month, day, and year
    if len(parts) == 3:
        month, day, year = parts[0], parts[1][:-1], parts[2]

        # check for month
        if month in months and day.isdigit() and year.isdigit():
            month_num = months[month]
            day, year = int(day), int(year)

            # find current date to compare
            curr_date = date.today()

            # check if the date is no later than the current date
            if (year < curr_date.year) or (year == curr_date.year and month_num < curr_date.month) or \
                    (year == curr_date.year and month_num == curr_date.month and day <= curr_date.day):
                return f"{month_num}/{day}/{year}"

    return None
