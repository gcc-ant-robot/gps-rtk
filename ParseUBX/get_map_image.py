ffrom mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

fig = plt.gcf()
# fig.set_size_inches(10, 15)
# Google map
map = Basemap(  llcrnrlon= -80.080208,
                llcrnrlat=  41.154397,
                urcrnrlon= -80.077010,
                urcrnrlat=  41.155810,
                epsg=2271)
map.arcgisimage(service='World_Imagery', verbose= True)

# Scatter of gps data in lat lon
# plt.title("Latitude vs. Longitude")
plt.show()
fig.savefig("Map.png", bbox_inches='tight', pad_inches = -.1, dpi=220)
