package com.s0hel.linkedlists;

import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class BrowserHistoryLinkedListTest {
    @Test
    public void testBrowserHistory() {
        BrowserHistoryLinkedList browserHistory = new BrowserHistoryLinkedList("leetcode.com");
        assertEquals("leetcode.com", browserHistory.getCurrentPage());

        browserHistory.visit("google.com");       // You are in "leetcode.com". Visit "google.com"
        assertEquals("google.com", browserHistory.getCurrentPage());
        assertEquals(2, browserHistory.getHistory().size());
        assertEquals("leetcode.com", browserHistory.getHistory().get(0));
        assertEquals("google.com", browserHistory.getHistory().get(1));

        browserHistory.visit("facebook.com");     // You are in "google.com". Visit "facebook.com"
        assertEquals("facebook.com", browserHistory.getCurrentPage());
        assertEquals(3, browserHistory.getHistory().size());
        assertEquals("leetcode.com", browserHistory.getHistory().get(0));
        assertEquals("google.com", browserHistory.getHistory().get(1));
        assertEquals("facebook.com", browserHistory.getHistory().get(2));

        browserHistory.visit("youtube.com");      // You are in "facebook.com". Visit "youtube.com"
        assertEquals("youtube.com", browserHistory.getCurrentPage());
        assertEquals(4, browserHistory.getHistory().size());
        assertEquals("leetcode.com", browserHistory.getHistory().get(0));
        assertEquals("google.com", browserHistory.getHistory().get(1));
        assertEquals("facebook.com", browserHistory.getHistory().get(2));
        assertEquals("youtube.com", browserHistory.getHistory().get(3));

        browserHistory.back(1);                   // You are in "youtube.com", move back to "facebook.com" return "facebook.com"
        assertEquals("facebook.com", browserHistory.getCurrentPage());
        assertEquals(4, browserHistory.getHistory().size());
        assertEquals("leetcode.com", browserHistory.getHistory().get(0));
        assertEquals("google.com", browserHistory.getHistory().get(1));
        assertEquals("facebook.com", browserHistory.getHistory().get(2));
        assertEquals("youtube.com", browserHistory.getHistory().get(3));

        browserHistory.back(1);                   // You are in "facebook.com", move back to "google.com" return "google.com"
        assertEquals("google.com", browserHistory.getCurrentPage());
        assertEquals(4, browserHistory.getHistory().size());
        assertEquals("leetcode.com", browserHistory.getHistory().get(0));
        assertEquals("google.com", browserHistory.getHistory().get(1));
        assertEquals("facebook.com", browserHistory.getHistory().get(2));
        assertEquals("youtube.com", browserHistory.getHistory().get(3));

        browserHistory.forward(1);                // You are in "google.com", move forward to "facebook.com" return "facebook.com"
        assertEquals("facebook.com", browserHistory.getCurrentPage());
        assertEquals(4, browserHistory.getHistory().size());
        assertEquals("leetcode.com", browserHistory.getHistory().get(0));
        assertEquals("google.com", browserHistory.getHistory().get(1));
        assertEquals("facebook.com", browserHistory.getHistory().get(2));
        assertEquals("youtube.com", browserHistory.getHistory().get(3));

        browserHistory.visit("linkedin.com");     // You are in "facebook.com". Visit "linkedin.com"
        assertEquals("linkedin.com", browserHistory.getCurrentPage());
        assertEquals(4, browserHistory.getHistory().size());
        assertEquals("leetcode.com", browserHistory.getHistory().get(0));
        assertEquals("google.com", browserHistory.getHistory().get(1));
        assertEquals("facebook.com", browserHistory.getHistory().get(2));
        assertEquals("linkedin.com", browserHistory.getHistory().get(3));

        browserHistory.forward(2);                // You are in "linkedin.com", you cannot move forward any steps.
        assertEquals("linkedin.com", browserHistory.getCurrentPage());
        assertEquals(4, browserHistory.getHistory().size());
        assertEquals("leetcode.com", browserHistory.getHistory().get(0));
        assertEquals("google.com", browserHistory.getHistory().get(1));
        assertEquals("facebook.com", browserHistory.getHistory().get(2));
        assertEquals("linkedin.com", browserHistory.getHistory().get(3));

        browserHistory.back(2);                   // You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"
        assertEquals("google.com", browserHistory.getCurrentPage());
        assertEquals(4, browserHistory.getHistory().size());
        assertEquals("leetcode.com", browserHistory.getHistory().get(0));
        assertEquals("google.com", browserHistory.getHistory().get(1));
        assertEquals("facebook.com", browserHistory.getHistory().get(2));
        assertEquals("linkedin.com", browserHistory.getHistory().get(3));

        browserHistory.back(7);                   // You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"
        assertEquals("leetcode.com", browserHistory.getCurrentPage());
        assertEquals(4, browserHistory.getHistory().size());
        assertEquals("leetcode.com", browserHistory.getHistory().get(0));
        assertEquals("google.com", browserHistory.getHistory().get(1));
        assertEquals("facebook.com", browserHistory.getHistory().get(2));
        assertEquals("linkedin.com", browserHistory.getHistory().get(3));
    }
}
