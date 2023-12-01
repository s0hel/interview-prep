package com.s0hel.hash;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class MyHashMap {

    private static class Entry {
        Integer key;
        Integer value;

        public Entry(Integer key, Integer value) {
            this.key = key;
            this.value = value;
        }
    }

    private int size;
    private int capacity;

    private ArrayList<LinkedList<Entry>> map;

    public MyHashMap() {
        capacity = 10000;
        map = new ArrayList<>(capacity);
        for (int i = 0; i < capacity; ++i) {
            map.add(new LinkedList<>());
        }
    }

    public void put(int key, int value) {
        int hash = Integer.hashCode(key);
        int index = hash % capacity;

        LinkedList<Entry> entries = map.get(index);

        boolean replaced = false;
        for (Entry entry : entries) {
            if (entry.key == key) {
                entry.value = value;
                replaced = true;
                break;
            }
        }

        if (!replaced) {
            entries.add(new Entry(key, value));
        }
    }

    public int get(int key) {
        int hash = Integer.hashCode(key);
        int index = hash % capacity;
        LinkedList<Entry> entries = map.get(index);

        for (Entry entry : entries) {
            if (entry.key == key) {
                return entry.value;
            }
        }

        return -1;
    }

    public void remove(int key) {
        int hash = Integer.hashCode(key);
        int index = hash % capacity;
        LinkedList<Entry> entries = map.get(index);

        for (int i = 0; i < entries.size(); ++i) {
            Entry entry = entries.get(i);
            if (entry.key == key) {
                entries.remove(i);
                break;
            }
        }
    }

}
