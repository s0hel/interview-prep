package com.s0hel.hash;

import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;
import java.util.List;

/*
705. Design HashSet

Design a HashSet without using any built-in hash table libraries.

Implement MyHashSet class:

void add(key) Inserts the value key into the HashSet.
bool contains(key) Returns whether the value key exists in the HashSet or not.
void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.


Example 1:

Input
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
Output
[null, null, null, true, false, null, true, null, false]

Explanation
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1);      // set = [1]
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(1); // return True
myHashSet.contains(3); // return False, (not found)
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(2); // return True
myHashSet.remove(2);   // set = [1]
myHashSet.contains(2); // return False, (already removed)
 */
public class MyHashSet {

    private final int capacity;
    private List<LinkedList<Integer>> array;

    public MyHashSet() {
        capacity = 10;
        array = new ArrayList<>(capacity);
        for (int i = 0; i < capacity; ++i) {
            array.add(new LinkedList<>());
        }
    }

    public void add(int key) {
        int idx = Integer.hashCode(key) % capacity;

//        if (array.get(idx) == null) {
//            array.add(idx, new LinkedList<>());
//        }

        LinkedList<Integer> values = array.get(idx);
        if (!values.contains(key)) {
            values.add(key);
        }
    }

    public void remove(int key) {
        int idx = Integer.hashCode(key) % capacity;

        LinkedList<Integer> values = array.get(idx);
        if (values != null) {
            values.remove(Integer.valueOf(key));
        }
    }

    public boolean contains(int key) {
        int idx = Integer.hashCode(key) % capacity;

        LinkedList<Integer> values = array.get(idx);

        return values != null && values.contains(key);
    }
}
