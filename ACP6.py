months = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

for month in months:
    print(month)


import calendar

for month in calendar.month_name[1:]:
    print(month)
for i in range(1, 13):
    print(calendar.month_name[i])