package com.s0hel.linkedlists;

import org.junit.Assert;
import org.junit.Test;

public class NumStudentsEatLunchTest {

    @Test
    public void testScenario() {
        NumStudentsEatLunch n = new NumStudentsEatLunch();

        int[] students = {1, 1, 1, 0, 0, 1};
        int[] sandwiches = {1, 0, 0, 0, 1, 1};

        Assert.assertEquals(3, n.countStudents(students, sandwiches));
    }
}
