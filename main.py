import datetime
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import numpy as np

months = mdates.MonthLocator()
days = mdates.DayLocator()
timeFmt = mdates.DateFormatter('%d.%m')
events = [datetime.date(2023, 4, 10),
          datetime.date(2023, 4, 11),
          datetime.date(2023, 4, 15),
          datetime.date(2023, 4, 19),
          datetime.date(2023, 4, 20),
          datetime.date(2023, 4, 21),
          datetime.date(2023, 4, 22),
          datetime.date(2023, 4, 23),
          datetime.date(2023, 4, 24),
          datetime.date(2023, 4, 25),
          datetime.date(2023, 4, 26),
          datetime.date(2023, 4, 27),
          datetime.date(2023, 4, 28),
          datetime.date(2023, 4, 29),
          datetime.date(2023, 4, 30),
          datetime.date(2023, 5, 1),
          datetime.date(2023, 5, 2),
          datetime.date(2023, 5, 3),
          datetime.date(2023, 5, 4),
          datetime.date(2023, 5, 5),
          datetime.date(2023, 5, 6),
          datetime.date(2023, 5, 7),
          datetime.date(2023, 5, 8),
          datetime.date(2023, 5, 9),
          datetime.date(2023, 5, 10),
          datetime.date(2023, 5, 11),
          datetime.date(2023, 5, 12),
          datetime.date(2023, 5, 13),
          datetime.date(2023, 5, 14),
          datetime.date(2023, 5, 15),
          datetime.date(2023, 5, 16),
          datetime.date(2023, 5, 17),
          datetime.date(2023, 5, 18),
          datetime.date(2023, 5, 19),
          datetime.date(2023, 5, 20),
          datetime.date(2023, 5, 21),
          datetime.date(2023, 5, 22),
          datetime.date(2023, 5, 23),
          datetime.date(2023, 5, 24),
          datetime.date(2023, 5, 25),
          datetime.date(2023, 5, 26),
          datetime.date(2023, 5, 27),
          datetime.date(2023, 5, 28),
          datetime.date(2023, 5, 29),
          datetime.date(2023, 5, 30),
          datetime.date(2023, 5, 31),
          datetime.date(2023, 6, 1),
          datetime.date(2023, 6, 2),
          datetime.date(2023, 6, 3),
          datetime.date(2023, 6, 4),
          datetime.date(2023, 6, 5),
          datetime.date(2023, 6, 6),
          datetime.date(2023, 6, 7),
          datetime.date(2023, 6, 8),
          datetime.date(2023, 6, 9),
          datetime.date(2023, 6, 10),
          datetime.date(2023, 6, 11),
          datetime.date(2023, 6, 12),
          datetime.date(2023, 6, 13),
          datetime.date(2023, 6, 14),
          datetime.date(2023, 6, 15),
          datetime.date(2023, 6, 16),
          datetime.date(2023, 6, 17),
          datetime.date(2023, 6, 18),
          datetime.date(2023, 6, 19)
          ]
readings = [1150, 1160, 1205, 1220, 1265, 1290, 1340, 1370, 1410, 1380, 1410, 1450, 1434, 1451, 1557,
            1616, 1678, 1755, 1748, 1790, 1825, 1870, 1870, 1900, 1915, 1915, 1985, 2005, 2085, 2110, 2130, 2150, 2180,
            2190, 2220, 2240,
            2280, 2280, 2305, 2315, 2365, 2370, 2425, 2440, 2480, 2480,
            2500, 2540, 2570, 2580, 2660, 2630, 2690, 2720,2780,2780,2810,2810,2890,2940,
            2940,2950,2950,3000,3000]

x = np.array([(event - events[0]).days for event in events])
y = np.array(readings)
a, b, c, d, e, f = np.polyfit(x, y, 5)
yy = a * x ** 5 + b * x ** 4 + c * x ** 3 + d * x ** 2 + e * x + f
fig, ax = plt.subplots()
plt.plot(events, readings, 'r.')
plt.plot(events, yy)
# ax.xaxis.set_major_locator(months)
ax.xaxis.set_major_formatter(timeFmt)
ax.xaxis.set_minor_locator(days)
plt.show()
#
# xx=np.array(list(range(50)))
# yy=a*xx**4+b*xx**3+c*xx**2+d*xx+e
# plt.plot(xx, yy)
# plt.show()
