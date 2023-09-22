package com.s0hel.linkedlists;

public class MergeTwoSortedLists {
    public static class ListNode {
        int val;
        ListNode next;

        ListNode() {
        }

        ListNode(int val) {
            this.val = val;
        }

        ListNode(int val, ListNode next) {
            this.val = val;
            this.next = next;
        }
    }

    /*
    You are given the heads of two sorted linked lists list1 and list2.

    Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

    Return the head of the merged linked list.

    Input: list1 = [1,2,4], list2 = [1,3,4]
    Output: [1,1,2,3,4,4]

    Example 2:

    Input: list1 = [], list2 = []
    Output: []

    Example 3:

    Input: list1 = [], list2 = [0]
    Output: [0]

     */

    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode result = new ListNode();
        ListNode current = result;

        ListNode pointer1 = list1;
        ListNode pointer2 = list2;

        while (pointer1 != null && pointer2 != null) {
            if (pointer1.val <= pointer2.val) {
                current.next = pointer1;
                pointer1 = pointer1.next;
            } else {
                current.next = pointer2;
                pointer2 = pointer2.next;
            }
            current = current.next;
        }

        if (pointer1 != null) {
            current.next = pointer1;
        }
        if (pointer2 != null) {
            current.next = pointer2;
        }

        return result.next;
    }
}
