package com.s0hel.linkedlists;

import java.util.ArrayList;
import java.util.List;

public class BrowserHistoryLinkedList {
    public static class Node {
        Node next, prev;
        String url;

        public Node(String url) {
            this.url = url;
        }
    }

    Node head, curr;

    /**
     * Initializes the object with the homepage of the browser.
     *
     * @param homepage - url
     */
    public BrowserHistoryLinkedList(String homepage) {
        head = new Node(homepage);
        curr = head;
    }

    /**
     * Visits url from the current page. It clears up all the forward history.
     */
    public void visit(String url) {
        Node node = new Node(url);
        node.prev = curr;
        curr.next = node;
        curr = node;
    }

    /**
     * Move steps back in history. If you can only return x steps in the history and steps > x,
     * you will return only x steps. Return the current url after moving back in history at most steps.
     */
    public String back(int steps) {
        for (int i = 0; i < steps && curr.prev != null; ++i) {
            curr = curr.prev;
        }
        return curr.url;
    }

    /**
     * Move steps forward in history. If you can only forward x steps in the history and steps > x, you will forward only x steps. Return the current url after forwarding in history at most steps.
     */
    public String forward(int steps) {
        for (int i = 0; i < steps && curr.next != null; ++i) {
            curr = curr.next;
        }
        return curr.url;
    }

    public String getCurrentPage() {
        return curr.url;
    }

    public List<String> getHistory() {
        List<String> history = new ArrayList<>();
        Node c = head;
        while (c != null) {
            history.add(c.url);
            c = c.next;
        }
        return history;
    }

}
