# https://www.geeksforgeeks.org/activity-selection-problem-greedy-algo-1/
from typing import List


# Problem:
# You are given n activities with their start and finish times. Select the maximum number of activities that can be performed by a single person, assuming that a person can only work on a single activity at a time.
#
# Examples:
#
# Input: start[]  =  {10, 12, 20}, finish[] =  {20, 25, 30}
# Output: 0
# Explanation: A person can perform at most one activities.
#
#
# Input: start[]  =  {1, 3, 0, 5, 8, 5}, finish[] =  {2, 4, 6, 7, 9, 9};
# Output: 0 1 3 4
# Explanation: A person can perform at most four activities. The
# maximum set of activities that can be executed
# is {0, 1, 3, 4} [ These are indexes in start[] and finish[]

# Prints a maximum set of activities that can be done
# by a single person, one at a time.
def printMaxActivities(start: List[int], finish: List[int]) -> List[int]:
    # sort based on finish times
    # select first activity from sorted array
    # print non-overlapping activities

    pairs = [[start[i], finish[i]] for i in range(len(start))]
    print(f"unsorted start/end times: {pairs}")
    pairs.sort(key=lambda x: x[1])
    print(f"sorted start/end times:   {pairs}")

    max_activities = []
    for i in range(len(pairs)):
        p = pairs[i]
        start_time = p[0]

        if i == 0:
            max_activities.append(p)
        else:
            prev_end_time = max_activities[-1][1]
            if start_time >= prev_end_time:
                max_activities.append(p)

    print(f"Num of max activities:    {len(max_activities)}\nactivities:               {max_activities}")


printMaxActivities([1, 2, 4, 6, 8, 9, 10], [20, 3, 5, 7, 12, 11, 12])
printMaxActivities([10, 12, 20], [20, 25, 30])
printMaxActivities([1, 3, 0, 5, 8, 5], [2, 4, 6, 7, 9, 9])
