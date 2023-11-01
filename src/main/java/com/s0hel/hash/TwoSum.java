package com.s0hel.hash;

/*
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

 */

import java.util.HashMap;
import java.util.Map;

public class TwoSum {
    public int[] twoSum(int[] nums, int target) {
//        for (int i = 0; i < nums.length; ++i) {
//            for (int j = i + 1; j < nums.length; ++j) {
//                if (nums[i] + nums[j] == target) {
//                    return new int[] {i, j};
//                }
//            }
//        }
//
//        return null;

        Map<Integer, Integer> numsMap = new HashMap<>();

        int other;
        for (int i = 0; i < nums.length; ++i) {
            other = target - nums[i];
            if (numsMap.containsKey(other)) {
                return new int[]{numsMap.get(other), i};
            }
            numsMap.put(nums[i], i);
        }

        return null;
    }
}
