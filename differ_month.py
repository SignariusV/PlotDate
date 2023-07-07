import datetime
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
delta=30
name='weight'
dates=[]
values=[]
with open(f'{name}.txt') as file:
    for str_line in file.readlines():
        date, value=str_line.split('_')
        dates.append(datetime.date(*list(map(int, date.split(',')))))
        values.append(int(value))
delta_month=datetime.timedelta(days=delta)
differ_date=[]
differ_value=[]

for date in dates:
    if (current:=date+delta_month) in dates:
        differ_date.append(current)
        i_1=dates.index(date)
        i_2=dates.index(current)
        differ_value.append(values[i_2]-values[i_1])


months = mdates.MonthLocator()
days = mdates.DayLocator()
timeFmt = mdates.DateFormatter('%d.%m')


x = np.array([(event - differ_date[0]).days for event in differ_date])
y = np.array(differ_value)
a, b, c, d, e= np.polyfit(x, y, 4)
yy = a * x ** 4 + b * x**3 + c*x**2+d*x+e
fig, ax = plt.subplots()
plt.plot(differ_date, differ_value, 'r')
plt.plot(differ_date, yy)
# ax.xaxis.set_major_locator(months)
ax.xaxis.set_major_formatter(timeFmt)
ax.xaxis.set_minor_locator(days)
plt.show()