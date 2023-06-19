import datetime
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
dates=[]
values=[]
file_name='weight.txt'
with open(file_name) as file:
    for str_line in file.readlines():
        date, value=str_line.split('_')
        dates.append(datetime.date(*list(map(int, date.split(',')))))
        values.append(int(value))


months = mdates.MonthLocator()
days = mdates.DayLocator()
timeFmt = mdates.DateFormatter('%d.%m')


x = np.array([(event - dates[0]).days for event in dates])
y = np.array(values)
a, b, c= np.polyfit(x, y, 2)
print(a,b,c)
yy = a * x ** 2 + b * x + c
fig, ax = plt.subplots()
plt.plot(dates, values, 'r.')
plt.plot(dates, yy)
# ax.xaxis.set_major_locator(months)
ax.xaxis.set_major_formatter(timeFmt)
ax.xaxis.set_minor_locator(days)
plt.show()

