package com.s0hel.linkedlists;

/**
 * Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
 * A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
 * If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.
 * <p>
 * Implement the MyLinkedList class:
 * <p>
 * MyLinkedList() Initializes the MyLinkedList object.
 * int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
 * void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
 * void addAtTail(int val) Append a node of value val as the last element of the linked list.
 * void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
 * void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.
 * <p>
 * <p>
 * Example 1:
 * <p>
 * Input
 * ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
 * [[], [1], [3], [1, 2], [1], [1], [1]]
 * Output
 * [null, null, null, null, 2, null, 3]
 * <p>
 * Explanation
 * MyLinkedList myLinkedList = new MyLinkedList();
 * myLinkedList.addAtHead(1);
 * myLinkedList.addAtTail(3);
 * myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
 * myLinkedList.get(1);              // return 2
 * myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
 * myLinkedList.get(1);              // return 3
 */

public class MyLinkedList {

    public static class Node {
        Node prev;
        Node next;
        int val;

        public Node(int val, Node next, Node prev) {
            this.prev = prev;
            this.next = next;
            this.val = val;
        }
    }

    Node head = null;
    Node tail = null;
    int size = 0;

    public MyLinkedList() {
    }

    public int get(int index) {
        try {
            Node curr = getNode(index);
            assert curr != null;
            return curr.val;
        } catch (IndexOutOfBoundsException ex) {
            ex.printStackTrace();
            return -1;
        }
    }

    public void addAtHead(int val) {
        Node node = new Node(val, head, null);
        if (size > 0) {
            head.prev = node;
        }
        head = node;
        size++;
        if (size == 1) {
            tail = head;
        }
    }

    public void addAtTail(int val) {
        Node node = new Node(val, null, tail);
        if (size > 0) {
            tail.next = node;
        }
        tail = node;
        size++;
        if (size == 1) {
            head = tail;
        }
    }

    public void addAtIndex(int index, int val) {
        if (index == 0) {
            addAtHead(val);
        } else {
            if (index == size) {
                addAtTail(val);
            } else {
                try {
                    Node curr = getNode(index);
                    Node prev = curr.prev;
                    Node node = new Node(val, curr, prev);
                    prev.next = node;
                    curr.prev = node;
                    size++;
                } catch (IndexOutOfBoundsException ex) {
                    ex.printStackTrace();
                    // instructions says to simply not insert.
                }
            }
        }
    }

    public void deleteAtIndex(int index) {
        try {
            Node curr = getNode(index);
            Node prev = curr.prev;
            Node next = curr.next;

            if (prev == null) { // must be the head
                if (next != null) {
                    head = next;
                    next.prev = null;
                } else {
                    head = null;
                    tail = null;
                }
            } else if (next == null) { // must be at the tail
                prev.next = null;
                tail = prev;
            } else {
                prev.next = next;
                next.prev = prev;
            }

            size--;
        } catch (IndexOutOfBoundsException ex) {
            ex.printStackTrace();
            // dont do anything if index is invalid
        }
    }

    private Node getNode(int index) {
        if (index < 0 || index >= size) {
            throw new IndexOutOfBoundsException("Index out of bounds: " + index + ", size: " + size);
        }

        Node curr = head;
        int i = 0;
        while (curr != null) {
            if (i == index) {
                break;
            }
            curr = curr.next;
            ++i;
        }

        return curr;
    }

}


/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList obj = new MyLinkedList();
 * int param_1 = obj.get(index);
 * obj.addAtHead(val);
 * obj.addAtTail(val);
 * obj.addAtIndex(index,val);
 * obj.deleteAtIndex(index);
 */