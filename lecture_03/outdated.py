
def get_date_input():
    # list of months for conversion
    months_list = [
        "january", "february", "march", "april", "may", "june", "july", "august",
        "september", "october", "november", "december"
    ]

    while True:
        # prompt user for date input
        date_str = input("Date (MM/DD/YYYY) or (Month Day, Year): ").strip()

        try:
            # check for "MM/DD/YYYY" format
            if "/" in date_str:
                month, day, year = date_str.split("/")
                month = int(month)
                day = int(day)
                year = int(year)

                # ensure valid ranges for month, day and year
                if 1 <= month <= 12 and 1 <= day <= 31 and year > 0:
                    # return formatted date
                    return f"{year:04}-{month:02}-{day:02}"

            # check for "Month Day, Year" format
            elif "," in date_str:
                month_day, year = date_str.split(",")
                month_name, day = month_day.split(" ")

                month = months_list.index(month_name.lower()) + 1
                day = int(day)
                year = int(year)

                # ensure valid ranges for day and year
                if 1 <= day <= 31 and year > 0:
                    # return formatted date
                    return f"{year:04}-{month:02}-{day:02}"

        except (ValueError, IndexError):
            # if parsing fails or invalid data, prompt again
            pass

        # print error and loop if error occurs
        print("ERROR: Invalid date format, try again.")

def main():
    while True:
        print(get_date_input())

if __name__ == '__main__':
    main()