package com.s0hel.hash;

import java.util.HashSet;
import java.util.Set;

public class Duplicates {
    public boolean containsDuplicate(int[] nums) {

        Set<Integer> set = new HashSet<>();

        for (int num : nums) {
            if (set.contains(num)) {
                return false;
            } else {
                set.add(num);
            }
        }

        return true;
    }

}
