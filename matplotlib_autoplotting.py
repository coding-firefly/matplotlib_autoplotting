import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#.csv file as input, full dir
gas= pd.read_csv("csv_file_here")

#plotting configuration
plt.figure(figsize=(5,3), dpi= 100)

plt.title("Copper Price")
#----- for automatic plotting Graph -----
for country in copper:
    if country != "Year":
        plt.plot(copper.Year, copper[country], label=country, marker=".")        
#----- -----

plt.xticks(copper.Year[::3])
#assume gap of every 3 years

plt.xlabel("Years")
#label for xAxis

plt.legend()
plt.show()
