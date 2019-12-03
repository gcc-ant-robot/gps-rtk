import parse
import numpy as np

fn1 = "data/day1/nov_5_location1.ubx"
positions1, edges = parse.process_ubx_file(fn1)
parse.plot_ubx_file(fn1, out_fn="loc1.png")
positions1_ecef = parse.positions_LLA_to_ECEF_point(positions1)

fn2 = "data/day1/nov_5_location6.ubx"
positions2, edges = parse.process_ubx_file(fn2)
parse.plot_ubx_file(fn2, out_fn="loc2.png")
positions2_ecef = parse.positions_LLA_to_ECEF_point(positions2)

a = np.linalg.norm(positions2_ecef - positions1_ecef)
# a = a * 1000 # km to meters
a = a * 39.3701 # meters to in
print("Distance between the means of the two .ubx files given by pyProj: {:.2f}\"".format(a))

a = parse.distance_between_ubx_inches(positions1, positions2)
print("Distance between the means of the two .ubx files given by my code: {:.2f}\"".format(
    np.linalg.norm(a)))

