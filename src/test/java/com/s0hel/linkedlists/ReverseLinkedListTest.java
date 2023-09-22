package com.s0hel.linkedlists;

import com.s0hel.linkedlists.ReverseLinkedList.ListNode;
import org.junit.Assert;
import org.junit.Test;

public class ReverseLinkedListTest {

    @Test
    public void testReverse() {
        ReverseLinkedList rll = new ReverseLinkedList();

        ListNode head = new ListNode(1,
                new ListNode(2,
                new ListNode(3,
                new ListNode(4,
                new ListNode(5)))));

        ListNode result = rll.reverseList(head);

        Assert.assertEquals(5, result.val);
        Assert.assertEquals(4, result.next.val);
        Assert.assertEquals(3, result.next.next.val);
        Assert.assertEquals(2, result.next.next.next.val);
        Assert.assertEquals(1, result.next.next.next.next.val);

        head = new ListNode(1,new ListNode(2));

        result = rll.reverseList(head);
        Assert.assertEquals(2, result.val);
        Assert.assertEquals(1, result.next.val);

        result = rll.reverseList(new ListNode());
        Assert.assertEquals(0, result.val);

    }
}
