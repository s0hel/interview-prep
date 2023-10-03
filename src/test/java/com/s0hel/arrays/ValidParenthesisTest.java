package com.s0hel.arrays;

import org.junit.Assert;
import org.junit.Test;

public class ValidParenthesisTest {

    @Test
    public void isValidTest() {
        ValidParenthesis vp = new ValidParenthesis();

        String test = "()";
        Assert.assertTrue(vp.isvalid(test));

        test = "()[]{}";
        Assert.assertTrue(vp.isvalid(test));

        test = "(]";
        Assert.assertFalse(vp.isvalid(test));

        test = "]";
        Assert.assertFalse(vp.isvalid(test));

        test = "){";
        Assert.assertFalse(vp.isvalid(test));

        test = "({[]})";
        Assert.assertTrue(vp.isvalid(test));

    }
}
