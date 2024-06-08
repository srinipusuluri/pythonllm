from datetime import date, datetime, time, timedelta

# date class methods and operations

# Creating a date object
my_date = date(2023, 5, 24)
print("Original date:", my_date)  # Output: 2023-05-24

# today()
print("Today's date:", date.today())  # Output: Current date

# fromtimestamp()
timestamp = 1633072800
print("Date from timestamp:", date.fromtimestamp(timestamp))  # Output: 2021-10-01

# replace()
new_date = my_date.replace(year=2024)
print("Replaced year:", new_date)  # Output: 2024-05-24

# timetuple()
print("Time tuple:", my_date.timetuple())  # Output: time.struct_time(...)

# toordinal()
print("Ordinal date:", my_date.toordinal())  # Output: 738226

# weekday()
print("Weekday:", my_date.weekday())  # Output: 2 (Wednesday)

# isoweekday()
print("ISO Weekday:", my_date.isoweekday())  # Output: 3 (Wednesday)

# isoformat()
print("ISO format:", my_date.isoformat())  # Output: 2023-05-24

# ctime()
print("C time:", my_date.ctime())  # Output: Wed May 24 00:00:00 2023

# strftime()
print("Formatted date:", my_date.strftime("%A, %B %d, %Y"))  # Output: Wednesday, May 24, 2023

# datetime class methods and operations

# Creating a datetime object
my_datetime = datetime(2023, 5, 24, 15, 30, 45)
print("Original datetime:", my_datetime)  # Output: 2023-05-24 15:30:45

# now()
print("Current datetime:", datetime.now())  # Output: Current datetime

# utcnow()
print("Current UTC datetime:", datetime.utcnow())  # Output: Current UTC datetime

# fromtimestamp()
print("Datetime from timestamp:", datetime.fromtimestamp(timestamp))  # Output: 2021-10-01 00:00:00

# combine()
comb_date = date(2023, 5, 24)
comb_time = time(15, 30, 45)
combined = datetime.combine(comb_date, comb_time)
print("Combined datetime:", combined)  # Output: 2023-05-24 15:30:45

# strptime()
date_string = "24-05-2023 15:30:45"
format_string = "%d-%m-%Y %H:%M:%S"
parsed_datetime = datetime.strptime(date_string, format_string)
print("Parsed datetime:", parsed_datetime)  # Output: 2023-05-24 15:30:45

# replace()
new_datetime = my_datetime.replace(year=2024)
print("Replaced datetime:", new_datetime)  # Output: 2024-05-24 15:30:45

# date()
print("Date part:", my_datetime.date())  # Output: 2023-05-24

# time()
print("Time part:", my_datetime.time())  # Output: 15:30:45

# timetuple()
print("Time tuple:", my_datetime.timetuple())  # Output: time.struct_time(...)

# isoformat()
print("ISO format datetime:", my_datetime.isoformat())  # Output: 2023-05-24T15:30:45

# ctime()
print("C time datetime:", my_datetime.ctime())  # Output: Wed May 24 15:30:45 2023

# strftime()
print("Formatted datetime:", my_datetime.strftime("%A, %B %d, %Y %H:%M:%S"))  # Output: Wednesday, May 24, 2023 15:30:45

# timedelta operations

# Creating a timedelta object
delta = timedelta(days=5, hours=3, minutes=30)
print("Timedelta:", delta)  # Output: 5 days, 3:30:00

# Adding timedelta to datetime
new_datetime = my_datetime + delta
print("Datetime after adding timedelta:", new_datetime)  # Output: 2023-05-29 19:00:45

# Subtracting timedelta from datetime
new_datetime = my_datetime - delta
print("Datetime after subtracting timedelta:", new_datetime)  # Output: 2023-05-19 12:00:45

# Difference between two datetime objects
datetime1 = datetime(2023, 5, 24, 15, 30, 45)
datetime2 = datetime(2023, 5, 20, 12, 0, 0)
difference = datetime1 - datetime2
print("Difference between datetimes:", difference)  # Output: 4 days, 3:30:45

# Total seconds in timedelta
print("Total seconds in timedelta:", delta.total_seconds())  # Output: 447000.0

# Min, max, and resolution
print("Minimum date:", date.min)  # Output: 0001-01-01
print("Maximum date:", date.max)  # Output: 9999-12-31
print("Date resolution:", date.resolution)  # Output: 1 day

print("Minimum datetime:", datetime.min)  # Output: 0001-01-01 00:00:00
print("Maximum datetime:", datetime.max)  # Output: 9999-12-31 23:59:59.999999
print("Datetime resolution:", datetime.resolution)  # Output: 0:00:00.000001
