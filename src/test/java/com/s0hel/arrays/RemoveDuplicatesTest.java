package com.s0hel.arrays;

import com.sohel.arrays.RemoveDuplicates;
import org.junit.Assert;
import org.junit.Test;

public class RemoveDuplicatesTest {

    @Test
    public void testRemoveDuplicates() {
        int[] array = {0, 1, 1, 2};
        int[] expected = {0, 1, 2, 0};

        RemoveDuplicates rd = new RemoveDuplicates();
        rd.removeDuplicates(array);
        Assert.assertArrayEquals(expected, array);
    }

    @Test
    public void testRemoveDuplicates2() {
        int[] array =    {0, 1, 1, 2, 2, 2, 3, 4, 4};
        int[] expected = {0, 1, 2, 3, 4, 0, 0, 0, 0};

        RemoveDuplicates rd = new RemoveDuplicates();
        rd.removeDuplicates(array);
        Assert.assertArrayEquals(expected, array);
    }

}
