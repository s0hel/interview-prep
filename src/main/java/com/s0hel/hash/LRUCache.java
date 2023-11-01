package com.s0hel.hash;

import java.util.HashMap;
import java.util.LinkedHashSet;

public class LRUCache {
    private final HashMap<Integer, Integer> map;
    private final LinkedHashSet<Integer> keyTracker;
    private final int capacity;

    public LRUCache(int capacity) {
        map = new HashMap<>(capacity);
        keyTracker = new LinkedHashSet<>(capacity);

        this.capacity = capacity;
    }

    public int get(int key) {
        System.out.println("get(" + key + ")");

        if (keyTracker.contains(key)) {
            keyTracker.remove(key);
            keyTracker.add(key);
            return map.get(key);
        }

        return -1;
    }

    public void put(int key, int value) {
        System.out.println("put(" + key + ", " + value + ")");

        if (!map.containsKey(key)) {
            if (this.map.size() == capacity) {
                int minKey = keyTracker.iterator().next();

                // evict minKey
                keyTracker.remove(minKey);
                map.remove(minKey);
            }

        } else {
            keyTracker.remove(key);
        }

        keyTracker.add(key);
        map.put(key, value);
    }

    protected void dump() {
        System.out.println("Map: " + map);
        System.out.println("KEY LRU: " + keyTracker);
        System.out.println("********");
    }

    public HashMap<Integer, Integer> getMap() {
        return map;
    }


    public int getCapacity() {
        return capacity;
    }
}
