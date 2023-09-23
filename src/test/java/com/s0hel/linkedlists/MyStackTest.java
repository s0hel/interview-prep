package com.s0hel.linkedlists;

import org.junit.Test;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;

public class MyStackTest {

    @Test
    public void testOperations() {
        MyStack myStack = new MyStack();
        myStack.push(1);
        myStack.push(2);
        assertEquals(2, myStack.top()); // return 2
        assertEquals(2, myStack.pop()); // return 2
        assertFalse(myStack.empty()); // return False
    }
}
