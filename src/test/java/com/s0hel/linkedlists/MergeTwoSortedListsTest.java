package com.s0hel.linkedlists;

import com.s0hel.linkedlists.MergeTwoSortedLists.ListNode;
import org.junit.Assert;
import org.junit.Test;

public class MergeTwoSortedListsTest {

    @Test
    public void testMerge() {
        ListNode list1 = new ListNode(1, new ListNode(2, new ListNode(4)));
        ListNode list2 = new ListNode(1, new ListNode(3, new ListNode(4)));

        MergeTwoSortedLists m = new MergeTwoSortedLists();
        ListNode result = m.mergeTwoLists(list1, list2);
        Assert.assertEquals(1, result.val);
        Assert.assertEquals(1, result.next.val);
        Assert.assertEquals(2, result.next.next.val);
        Assert.assertEquals(3, result.next.next.next.val);
        Assert.assertEquals(4, result.next.next.next.next.val);
        Assert.assertEquals(4, result.next.next.next.next.next.val);
    }
}
