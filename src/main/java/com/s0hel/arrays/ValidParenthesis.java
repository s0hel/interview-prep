package com.s0hel.arrays;

import java.util.LinkedList;
import java.util.List;

public class ValidParenthesis {
    /*
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false

Example 4:
Input s = "([])"
Output: true
     */
    public boolean isvalid(String s) {
        List<Character> stack = new LinkedList<>();
        for (int i = 0; i < s.length(); ++i) {
            switch (s.charAt(i)) {
                case '[', '{', '(' -> stack.add(s.charAt(i));
                case ']' -> {
                    if (!stack.isEmpty() && stack.get(stack.size() - 1) == '[') {
                        stack.remove(stack.size() - 1);
                    } else {
                        return false;
                    }
                }
                case '}' -> {
                    if (!stack.isEmpty() && stack.get(stack.size() - 1) == '{') {
                        stack.remove(stack.size() - 1);
                    } else {
                        return false;
                    }
                }
                case ')' -> {
                    if (!stack.isEmpty() && stack.get(stack.size() - 1) == '(') {
                        stack.remove(stack.size() - 1);
                    } else {
                        return false;
                    }
                }
            }
        }

        return stack.size() == 0;
    }
}
