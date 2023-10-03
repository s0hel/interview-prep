package com.s0hel.arrays;

public class RemoveDuplicates {

    public int removeDuplicates(int[] nums) {
        int uniqueIndex = 0;
        for (int i = 1; i < nums.length; ++i) {
            if (nums[i] != nums[uniqueIndex]) {
                uniqueIndex++;
                nums[uniqueIndex] = nums[i];
            }
        }

        // fill out the rest of the array with 0s
        for (int i = uniqueIndex + 1; i < nums.length; ++i) {
            nums[i] = 0;
        }

        return uniqueIndex + 1;
    }
}
