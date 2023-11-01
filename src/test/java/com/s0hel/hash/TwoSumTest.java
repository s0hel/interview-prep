package com.s0hel.hash;

import org.junit.Assert;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class TwoSumTest {

    @Test
    public void twoSumTest() {
        TwoSum ts = new TwoSum();
        int[] nums = {3, 2, 4};
        int[] result = ts.twoSum(nums, 6);

        assertEquals(1, result[0]);
        assertEquals(2, result[1]);
    }
}
