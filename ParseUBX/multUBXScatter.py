import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import geopy.distance # uses ellipsoid model of earth for better accuracy
# https://stackoverflow.com/questions/19412462/getting-distance-between-two-points-based-on-latitude-longitude/43211266#43211266
import parse

# fig, positions, edges = parse.scatter_ubx_file("data/day1/nov_5_location1_noDGNSS.ubx")

# fig = plt.gcf()
# fig.set_size_inches(8, 8)
# zoom = 14*12

labels = ['nov_5_location1_noDGNSS.ubx','nov_5_location1.ubx','nov_5_location2.ubx',
            'nov_5_location4.ubx','nov_5_location5.ubx',
            'nov_5_location6.ubx','nov_5_location7.ubx','nov_5_location8.ubx']
colors = ['r','g','g','b','b','g','g','b'] # red: NO RTK, Blue: float or no LOS, green: RTK float or fixed

offset = [0, 0]
for i in [1,2]:
    print("{},{}".format(labels[i], colors[i]))

    if colors[i] == 'g':
        positions, edges = parse.process_ubx_file("data/day1/{}".format(labels[i]))
        positions = parse.positions_to_inches(positions)
        # plt.scatter(positions[:,1],positions[:,0], label=labels[i],color=colors[i], s = 2)
    # plt.title("Location Drift over 2 Minutes [Inches]\n Red -> NO RTK, Blue -> RTK Float, Green -> RTK Fixed")



# dlat, dlon = np.mean(positions[:,0]),np.mean(positions[:,1])

# plt.plot([0,dlon], [0,dlat], ls='dashdot', color=[.5,.5,.5])

# th2 = plt.text(dlon/2, dlat/2, 'True Distance: {:.2f}\n Measured Distance: {:.2f}\n Error: {:.1f}%'.format(
#     165, np.sqrt(dlon**2 + dlat**2), (np.sqrt(dlon**2 + dlat**2) - 165)/165 * 100
# ), fontsize=16)

# plt.xlim((-zoom, zoom))
# plt.ylim((-zoom, zoom))
# plt.grid()
# plt.legend()
# fig = plt.gca()
# plt.savefig("global_scatter.png", dpi=220)

# plt.show()
