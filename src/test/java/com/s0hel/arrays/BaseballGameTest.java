package com.s0hel.arrays;

import com.sohel.arrays.BaseballGame;
import org.junit.Assert;
import org.junit.Test;

public class BaseballGameTest {

    @Test
    public void calPointsTest() {
        String[] input = {"5", "2", "C", "D", "+"};
        int expected = 30;

        BaseballGame bg = new BaseballGame();
        int result = bg.calPoints(input);

        Assert.assertEquals(expected, result);

        String[] input2 = {"5", "-2", "4", "C", "D", "9", "+", "+"};
        expected = 27;
        result = bg.calPoints(input2);

        Assert.assertEquals(expected, result);

        String[] input3= {"1", "C"};
        expected = 0;
        result = bg.calPoints(input3);

        Assert.assertEquals(expected, result);
    }
}
