package com.s0hel.recursion;

import org.junit.Assert;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class ClimbingStairsTest {
    @Test
    public void climbStairs() {
        ClimbingStairs c = new ClimbingStairs();

        assertEquals(2, c.climbStairs(2));
        assertEquals(3, c.climbStairs(3));
        assertEquals(5, c.climbStairs(4));
        assertEquals(8, c.climbStairs(5));
        assertEquals(13, c.climbStairs(6));
    }

}
