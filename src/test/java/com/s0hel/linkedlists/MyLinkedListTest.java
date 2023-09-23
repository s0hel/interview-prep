package com.s0hel.linkedlists;

import org.junit.Assert;
import org.junit.Test;

import static org.junit.Assert.*;

public class MyLinkedListTest {

    @Test
    public void testOperations() {
        MyLinkedList list = new MyLinkedList();
        list.addAtHead(1);
        assertEquals(1, list.size);
        assertEquals(1, list.head.val);
        assertSame(list.tail, list.head);

        list.addAtTail(3);
        assertEquals(2, list.size);
        assertEquals(1, list.head.val);
        assertEquals(3, list.tail.val);
        assertSame(list.head.next, list.tail);
        assertSame(list.tail.prev, list.head);

        list.addAtIndex(1, 2);    // linked list becomes 1->2->3
        assertEquals(3, list.size);
        assertEquals(1, list.head.val);
        assertEquals(2, list.head.next.val);
        assertEquals(3, list.tail.val);
        assertSame(list.head.next.next, list.tail);
        assertSame(list.head.next.prev, list.head);
        assertSame(list.tail.prev, list.head.next);

        int result = list.get(1);              // return 2
        assertEquals(2, result);

        list.deleteAtIndex(1);    // now the linked list is 1->3
        assertEquals(2, list.size);
        assertEquals(1, list.head.val);
        assertEquals(3, list.tail.val);
        assertSame(list.head.next, list.tail);
        assertSame(list.tail.prev, list.head);

        result = list.get(1);              // return 3
        assertEquals(3, result);
    }

    @Test
    public void testCase2() {
        MyLinkedList list = new MyLinkedList();
        list.addAtHead(7);           // 7
        assertEquals(1, list.size);
        assertEquals(7, list.get(0));

        list.addAtHead(2);           // 2 -> 7
        assertEquals(2, list.size);
        assertEquals(2, list.get(0));
        assertEquals(7, list.get(1));

        list.addAtHead(1);           // 1 -> 2 -> 7
        assertEquals(3, list.size);
        assertEquals(1, list.get(0));
        assertEquals(2, list.get(1));
        assertEquals(7, list.get(2));

        list.addAtIndex(3, 0); // 1 -> 2 -> 7 -> 0
        assertEquals(4, list.size);
        assertEquals(1, list.get(0));
        assertEquals(2, list.get(1));
        assertEquals(7, list.get(2));
        assertEquals(0, list.get(3));

        list.deleteAtIndex(2);           // 1 -> 2 -> 0
        assertEquals(3, list.size);
        assertEquals(1, list.get(0));
        assertEquals(2, list.get(1));
        assertEquals(0, list.get(2));

        list.addAtHead(6);           // 6 -> 1 -> 2 -> 0
        assertEquals(4, list.size);
        assertEquals(6, list.get(0));
        assertEquals(1, list.get(1));
        assertEquals(2, list.get(2));
        assertEquals(0, list.get(3));

        list.addAtTail(4);           // 6 -> 1 -> 2 -> 0 -> 4
        assertEquals(5, list.size);
        assertEquals(6, list.get(0));
        assertEquals(1, list.get(1));
        assertEquals(2, list.get(2));
        assertEquals(0, list.get(3));
        assertEquals(4, list.get(4));

        list.addAtHead(4);           // 4 -> 6 -> 1 -> 2 -> 0 -> 4
        assertEquals(6, list.size);
        assertEquals(4, list.get(0));
        assertEquals(6, list.get(1));
        assertEquals(1, list.get(2));
        assertEquals(2, list.get(3));
        assertEquals(0, list.get(4));
        assertEquals(4, list.get(5));

        list.addAtIndex(5, 0); // 4 -> 6 -> 1 -> 2 -> 0 -> 0 -> 4
        assertEquals(7, list.size);
        assertEquals(4, list.get(0));
        assertEquals(6, list.get(1));
        assertEquals(1, list.get(2));
        assertEquals(2, list.get(3));
        assertEquals(0, list.get(4));
        assertEquals(0, list.get(5));
        assertEquals(4, list.get(6));

        list.addAtHead(6);           // 6 -> 4 -> 6 -> 1 -> 2 -> 0 -> 0 -> 4
        assertEquals(8, list.size);
        assertEquals(6, list.get(0));
        assertEquals(4, list.get(1));
        assertEquals(6, list.get(2));
        assertEquals(1, list.get(3));
        assertEquals(2, list.get(4));
        assertEquals(0, list.get(5));
        assertEquals(0, list.get(6));
        assertEquals(4, list.get(7));
    }

    @Test
    public void testAddTail() {
        MyLinkedList list = new MyLinkedList();

        list.addAtTail(1);
        assertEquals(1, list.get(0));
    }
}
