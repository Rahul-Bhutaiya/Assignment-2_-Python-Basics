"""
Write a python script to display the current date and time. First create variables to
store date and time, then display date and time in proper format (like: 13-8-2022 and
9:00 PM)
"""
from datetime import datetime

x=datetime.now()
date=x.day
month=x.month
year=x.year
print(date,month,year,sep='-')

hour=x.hour
minutes=x.minute
seconds=x.second
am_pm=x.strftime('%p')
print(hour,':',minutes,':',seconds,' ',am_pm,sep='') 