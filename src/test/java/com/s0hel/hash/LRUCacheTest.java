package com.s0hel.hash;

import org.junit.Assert;
import org.junit.Test;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;

public class LRUCacheTest {

    @Test
    public void lruTest() {
        LRUCache lRUCache = new LRUCache(2);
        lRUCache.put(1, 1); // cache is {1=1}
        lRUCache.dump();

        lRUCache.put(2, 2); // cache is {1=1, 2=2}
        lRUCache.dump();

        System.out.println(lRUCache.get(1));    // return 1
        lRUCache.dump();

        lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
        lRUCache.dump();

        System.out.println(lRUCache.get(2));    // returns -1 (not found)
        lRUCache.dump();

        lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
        lRUCache.dump();

        System.out.println(lRUCache.get(1));    // return -1 (not found)
        lRUCache.dump();

        System.out.println(lRUCache.get(3));    // return 3
        lRUCache.dump();

        System.out.println(lRUCache.get(4));    // return 4
        lRUCache.dump();
    }

    @Test
    public void case14() {
        //["LRUCache","put","put","put","put","get","get"]
        //[[2],[2,1],[1,1],[2,3],[4,1],[1],[2]]

        LRUCache c = new LRUCache(2);

        c.put(2, 1);
        c.dump();
        assertEquals(1, (int) c.getMap().get(2));

        c.put(1, 1);
        c.dump();
        assertEquals(1, (int) c.getMap().get(2));
        assertEquals(1, (int) c.getMap().get(1));

        c.put(2, 3);
        c.dump();
        assertEquals(3, (int) c.getMap().get(2));
        assertEquals(1, (int) c.getMap().get(1));

        c.put(4, 1);
        c.dump();
        assertEquals(3, (int) c.getMap().get(2));
        assertEquals(1, (int) c.getMap().get(4));
        assertFalse(c.getMap().containsKey(1));

        assertEquals(-1, c.get(1));
        c.dump();

        assertEquals(3, c.get(2));
        c.dump();
    }
}
