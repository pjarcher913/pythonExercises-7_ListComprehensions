# Created by:   Patrick Archer
# Date:         21 December 2018
# Copyright to the above author. All rights reserved.

"""

Directions - COMPLETE:
Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.

"""

import random

# ################################################# start_funcs



# ################################################# end_funcs/start_main

# initial random list
random_list1 = []
for r1 in range(random.randrange(5, 50, 5, int)):
    random_list1.append(random.randrange(1, 100, 1, int))

print("\nRandomly-Generated List:\n" + str(random_list1))

# results list (even element values only)
evenElements = []

# "one line of Python that takes this list a and makes a new list that has only the even elements of this list in it"
evenElements = [random_list1[x] for x in range(len(random_list1)) if (random_list1[x] % 2 == 0)]

print("\nEven elements within the previously-described list:\n" + str(evenElements))

# ################################################# end_main





