package com.s0hel.arrays;

import java.util.ArrayList;
import java.util.List;

public class BaseballGame {
    /*
    You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.

You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:

An integer x.
Record a new score of x.
'+'.
Record a new score that is the sum of the previous two scores.
'D'.
Record a new score that is the double of the previous score.
'C'.
Invalidate the previous score, removing it from the record.
Return the sum of all the scores on the record after applying all the operations.

The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and that all operations are valid.



Example 1:

Input: ops = ["5","2","C","D","+"]
Output: 30
Explanation:
"5" - Add 5 to the record, record is now [5].
"2" - Add 2 to the record, record is now [5, 2].
"C" - Invalidate and remove the previous score, record is now [5].
"D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
"+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
The total sum is 5 + 10 + 15 = 30.
     */

    public int calPoints(String[] operations) {

        List<Integer> scores = new ArrayList<>();
        int sum = 0;
        for (String op : operations) {
            if ("+".equals(op)) {
                // record new score = sum of previous two scores
                int previous = scores.get(scores.size() - 1);
                int previous2 = scores.get(scores.size() - 2);
                scores.add(previous + previous2);
                sum += scores.get(scores.size()-1);
            } else if ("D".equals(op)) {
                // record new score = double of previous score
                int previous = scores.get(scores.size() - 1);
                scores.add(2 * previous);
                sum += scores.get(scores.size()-1);
            } else if ("C".equals(op)) {
                // cancel previous record
                sum -= scores.get(scores.size()-1);
                scores.remove(scores.size()-1);
            } else {
                // integer provided
                int value = Integer.parseInt(op);
                scores.add(value);
                sum += scores.get(scores.size()-1);
            }
        }

        return sum;
    }
}
