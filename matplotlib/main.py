import matplotlib.pyplot as plt
import numpy as np
from PIL.ImageColor import colormap
from matplotlib.lines import lineStyles

xpoint = np.array([2020,2021,2022,2023])
ypoint = np.array([6.6,5.5,8.8,8.9])

plt.plot(xpoint,ypoint)
plt.show()

plt.title('Indias GDP by the year')
plt.xlabel('year')
plt.ylabel('GDP')
plt.grid(color='brown',lineStyles='--',linewidth = 1)
plt.plot(xpoint,ypoint,color = 'red',alpha = 0.25)
plt.show()

