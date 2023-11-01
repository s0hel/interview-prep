package com.s0hel.heaps;


/*
973. K Closest Points to Origin

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).



Example 1:


Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.
 */

import java.util.Comparator;
import java.util.PriorityQueue;

public class KClosePointsOrigin {

    private static class PointComparator implements Comparator<int[]> {
        @Override
        public int compare(int[] o1, int[] o2) {
            int distance1 = (o1[0] * o1[0]) + (o1[1] * o1[1]);
            int distance2 = (o2[0] * o2[0]) + (o2[1] * o2[1]);
            return Integer.compare(distance2, distance1);
        }
    }

    public int[][] kClosest(int[][] points, int k) {
        PointComparator comparator = new PointComparator();
        PriorityQueue<int[]> maxHeap = new PriorityQueue<>(comparator);


        for (int[] point : points) {

            if (maxHeap.size() < k) {
                maxHeap.add(point);
            } else if (comparator.compare(point, maxHeap.peek()) > 0) {
                maxHeap.poll();
                maxHeap.add(point);
            }
        }

        int[][] result = new int[k][];

        int i = 0;
        for (int[] point : maxHeap) {
            result[i++] = point;
        }

        return result;
    }

}
