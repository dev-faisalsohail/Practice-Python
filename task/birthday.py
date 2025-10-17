from datetime import datetime, date

birth_str = input("Enter your birth date (YYYY-MM-DD): ")
birth_date = datetime.strptime(birth_str, "%Y-%m-%d").date()

today = date.today()
this_year_birthday = date(today.year, birth_date.month, birth_date.day)

if this_year_birthday < today:
    next_birthday = date(today.year + 1, birth_date.month, birth_date.day)
else:
    next_birthday = this_year_birthday

days_left = (next_birthday - today).days
print(f"🎉 Your next birthday is in {days_left} days!")

