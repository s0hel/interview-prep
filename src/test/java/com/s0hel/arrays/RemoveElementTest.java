package com.s0hel.arrays;

import com.sohel.arrays.RemoveElement;
import org.junit.Assert;
import org.junit.Test;

import java.util.Arrays;

public class RemoveElementTest {

    @Test
    public void removeElementTest() {
        int[] input = {3, 2, 2, 3};
        int[] expected = {2, 2};

        RemoveElement re = new RemoveElement();
        int result = re.removeElement(input, 3);
        Assert.assertEquals(expected.length, result);
        Assert.assertTrue(Arrays.equals(expected, 0, expected.length - 1, input, 0, expected.length - 1));
    }

    @Test
    public void removeElementTest2() {
        int[] input = {0, 1, 2, 2, 3, 0, 4, 2};
        int[] expected = {0, 1, 3, 0, 4};

        RemoveElement re = new RemoveElement();
        int result = re.removeElement(input, 2);
        Assert.assertEquals(expected.length, result);
        Assert.assertTrue(Arrays.equals(expected, 0, expected.length - 1, input, 0, expected.length - 1));
    }
}
