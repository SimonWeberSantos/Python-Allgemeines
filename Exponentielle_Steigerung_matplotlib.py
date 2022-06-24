# Exponentielle Steigerung

import matplotlib.pyplot

grafik = []

for zahl in range(101):
    zahlHochZwei = zahl**2
    grafik.append(zahlHochZwei)
    print(zahlHochZwei)

fig, ax = matplotlib.pyplot.subplots()
ax.grid(linestyle='-', linewidth='0.5', color='green')
matplotlib.pyplot.plot(grafik)
matplotlib.pyplot.yticks([100, 500, 1000, 3000, 6000, 10000])
matplotlib.pyplot.show()