import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
from annoy import AnnoyIndex

"""
## Planning: The Traveling Robot Problem

Visit a collection of points in the shortest path you can find. 
The catch? You have to "go home to recharge" every so often. 

We want fast approximations rather than a brute force perfect solution.
Your solution will be judged on:
* the length of path it produces
* fast runtime
* code quality and maintainability

### Details

* There are 5000 points distributed uniformly in [0, 1]
* The recharge station is located at (.5, .5)
* You cannot travel more than 3 units of distance before recharging
* You must start and end at the recharge station
* Skeleton code provided in Python. Python and C++ are acceptable
"""

#############################
home = np.array([0.5, 0.5])  # home is the recharging station
max_charge = 3.0
#############################

# generate the points to visit uniformly in [0,1]
# recharging station is index 0
N = 5000
pts = np.vstack((home, np.random.rand(N, 2)))


def check_order(pts, order):
    """Check whether a given order of points is valid, and prints the total
    length. You start and stop at the charging station.
    pts: np array of points to visit, prepended by the location of home
    order: array of pt indicies to visit, where 0 is home
    i.e. order = [0, 1, 0, 2, 0, 3, 0]"""

    print("Checking order")
    assert (pts.shape == (N + 1, 2))  # nothing weird
    assert (order[0] == 0)  # start path at home
    assert (order[-1] == 0)  # end path at home
    assert (set(order) == set(range(N + 1)))  # all pts visited

    print("Assertions passed")

    # traverse path
    total_d = 0
    charge = max_charge
    last = pts[0, :]

    for idx in order:
        pt = pts[idx, :]
        d = np.linalg.norm(pt - last)

        # update totals
        total_d += d
        charge -= d

        assert (charge > 0)  # out of battery

        # did we recharge?
        if idx == 0:
            charge = max_charge

        # moving to next point
        last = pt

    # We made it to end! path was valid
    print("Valid path!")
    print(total_d)
    draw_path(pts, order)


def draw_path(pts, order):
    """Draw the path to the screen"""
    path = pts[order, :]

    plt.plot(path[:, 0], path[:, 1])
    plt.show()


#############################
# Your code goes here
# Read the "pts" array
# generate a valid order, starting and ending with 0, the recharging station
#############################

def generate_order(pts):
    _order = []

    t = AnnoyIndex(2, 'euclidean')
    return _order


order = generate_order(pts)
check_order(pts, order)
