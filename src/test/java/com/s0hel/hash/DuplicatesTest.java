package com.s0hel.hash;

import org.junit.Assert;
import org.junit.Test;

public class DuplicatesTest {

    @Test
    public void containsDuplicatesTest() {
        int[] nums = {1, 2, 3, 1};

        Duplicates d = new Duplicates();
        Assert.assertFalse(d.containsDuplicate(nums));
    }
}
