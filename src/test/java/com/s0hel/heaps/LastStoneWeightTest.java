package com.s0hel.heaps;

import org.junit.Assert;
import org.junit.Test;

public class LastStoneWeightTest {

    @Test
    public void test() {
        LastStoneWeight s = new LastStoneWeight();
        int result = s.lastStoneWeight(new int[]{2, 7, 4, 1, 8, 1});

        Assert.assertEquals(1, result);

        result = s.lastStoneWeight(new int[]{1});
        Assert.assertEquals(1, result);
    }
}
