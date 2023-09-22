package com.s0hel.linkedlists;

import java.util.ArrayList;
import java.util.Stack;

public class ReverseLinkedList {

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
    Given the head of a singly linked list, reverse the list, and return the reversed list.
    Input: head = [1,2,3,4,5]
    Output: [5,4,3,2,1]

    Input: head = [1,2]
    Output: [2,1]

    Input: head = []
    Output: []
     */
    public ListNode reverseList(ListNode head) {

        ListNode newHead = null;
        ListNode curr = head;
        ListNode next;

        while (curr !=  null) {
            next = curr.next;

            curr.next = newHead;
            newHead = curr;

            curr = next;
        }

        return newHead;

        // 1, 2, 3, 4
        // newHead = null
        // curr = head = 1
        // pass 1
        // - next => 2
        // - curr.next = null
        // - newHead = 1
        // - curr = 2
        // pass 2
        // - next = 3
        // - curr.next = 1
        // - newHead = 2
        // - curr = 3
    }
}
