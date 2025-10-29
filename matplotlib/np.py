import numpy as np
import matplotlib.pyplot as plt
# x = np.linspace(-2,2,20)
# y = x**3
# plt.plot(x,y)
# plt.show()

# print(x)
# print(y)


chemical_exports = [0.810, 0.831, 0.895,0.91,0.915,0.926,0.945,0.931,0.97,0.99]


years = [2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]


medicine_exports = [0.710, 0.731, 0.795,0.81,0.315,0.426,0.645,0.531,0.97]


fig = plt.figure(figsize=(10,5))
fig,ax = plt.subplots()


ax.plot(years,chemical_exports,label="chemicals", marker='o', color='blue',linestyle='dashed', linewidth=2 )
ax.plot(years,medicine_exports,label="medicines", marker='x', color='orange',linestyle='solid', linewidth=2 )

ax.set_xlabel("Years")
ax.set_ylabel("Amount (Million US$)")


axvalues = np.array([2021,2020])
yvalues = np.array()([0.710,0.97])

ax.set_xticks(xvals)
ax.set_yticks(yvals)

plt.legend("chemicals","medicines")
plt.show()

print(chemical_exports)
print(years)

