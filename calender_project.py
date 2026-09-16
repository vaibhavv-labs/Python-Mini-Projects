import calendar

print("PYTHON CALENDAR")
print("_"*25)

year = int(input("Enter Year : "))
month = int(input("Enter Month (1-12) : "))

print("\n", calendar.month(year, month))
