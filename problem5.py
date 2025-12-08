# print a calender
import calendar
year=int(2025)
month=int(12)
cal=calendar.month(year,month)
print(cal)

# Area of triangle
base=float(25)
height=float(25)
area=0.5*base*height
print(area)

#converting kilomters into miles
kilo=float(100)
miles=kilo*0.621371
print(miles)

#swap two numbers without using temp variable
a=10
b=20
[a,b]=[b,a]
print(a,b)