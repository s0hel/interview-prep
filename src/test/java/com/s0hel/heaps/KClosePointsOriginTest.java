package com.s0hel.heaps;

import org.junit.Assert;
import org.junit.Test;

import java.util.Comparator;

import static org.junit.Assert.assertEquals;

public class KClosePointsOriginTest {




    @Test
    public void test() {
        KClosePointsOrigin s = new KClosePointsOrigin();


        int[][] points = {{1, 3}, {-2, 2}};
        int[][] result = s.kClosest(points, 1);

        assertEquals(-2, result[0][0]);
        assertEquals(2, result[0][1]);

        int[][] points2 = {{3, 3}, {5, -1}, {-2, 4}};
        result = s.kClosest(points2, 2);

        assertEquals(3, result[0][0]);
        assertEquals(3, result[0][1]);

        assertEquals(-2, result[1][0]);
        assertEquals(4, result[1][1]);
    }
}
