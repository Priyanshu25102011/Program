import calendar
import datetime

yy = 2025

print("Calendar of This Year")

for mm in range(1, 13):
    print(f"Calendar of {calendar.month_name[mm]}")
    print(calendar.month(yy, mm))


today = datetime.datetime.now()
print(f"Current Date and Time: {today}")