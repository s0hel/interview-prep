package com.s0hel.linkedlists;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

/**
 * The school cafeteria offers circular and square sandwiches at lunch break, referred to by numbers 0 and 1 respectively. All students stand in a queue. Each student either prefers square or circular sandwiches.
 * <p>
 * The number of sandwiches in the cafeteria is equal to the number of students. The sandwiches are placed in a stack. At each step:
 * <p>
 * If the student at the front of the queue prefers the sandwich on the top of the stack, they will take it and leave the queue.
 * Otherwise, they will leave it and go to the queue's end.
 * This continues until none of the queue students want to take the top sandwich and are thus unable to eat.
 * <p>
 * You are given two integer arrays students and sandwiches where sandwiches[i] is the type of the i​​​​​​th sandwich in the stack (i = 0 is the top of the stack) and students[j] is the preference of the j​​​​​​th student in the initial queue (j = 0 is the front of the queue). Return the number of students that are unable to eat.
 * <p>
 * <p>
 * <p>
 * Example 1:
 * <p>
 * Input: students = [1,1,0,0], sandwiches = [0,1,0,1]
 * Output: 0
 * Explanation:
 * - Front student leaves the top sandwich and returns to the end of the line making students = [1,0,0,1].
 * - Front student leaves the top sandwich and returns to the end of the line making students = [0,0,1,1].
 * - Front student takes the top sandwich and leaves the line making students = [0,1,1] and sandwiches = [1,0,1].
 * - Front student leaves the top sandwich and returns to the end of the line making students = [1,1,0].
 * - Front student takes the top sandwich and leaves the line making students = [1,0] and sandwiches = [0,1].
 * - Front student leaves the top sandwich and returns to the end of the line making students = [0,1].
 * - Front student takes the top sandwich and leaves the line making students = [1] and sandwiches = [1].
 * - Front student takes the top sandwich and leaves the line making students = [] and sandwiches = [].
 * Hence all students are able to eat.
 * Example 2:
 * <p>
 * Input: students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]
 * Output: 3
 * <p>
 * 1. students [1 1 0 0 1]   sandwiches [0 0 0 1 1]
 * 2. students [1 0 0 1 1]   sandwiches [0 0 0 1 1]
 * 3. students [0 0 1 1 1]   sandwiches [0 0 0 1 1]
 * 4. students [0 1 1 1]     sandwiches [0 0 1 1]
 * 5. students [1 1 1]       sandwiches [0 1 1]
 * => 3 students wont eat because no one will pick up the 0
 * Constraints:
 * <p>
 * 1 <= students.length, sandwiches.length <= 100
 * students.length == sandwiches.length
 * sandwiches[i] is 0 or 1.
 * students[i] is 0 or 1.
 */
public class NumStudentsEatLunch {

    public int countStudents(int[] students, int[] sandwiches) {
        Queue<Integer> stud = new LinkedList<>();
        Queue<Integer> sand = new LinkedList<>();

        for (int i = 0; i < students.length; ++i) {
            stud.add(students[i]);
            sand.add(sandwiches[i]);
        }


        int counter = 0;
        while (!stud.isEmpty() && !sand.isEmpty()) {
            int currentStudent = stud.peek();
            int currentSandwich = sand.peek();

            if (currentStudent == currentSandwich) {
                stud.poll();
                sand.poll();
                counter = 0;
            } else {
                // rotate students
                stud.add(stud.poll());
                counter++;
            }

            // if we cycled through the entire student queue, then these folks will never eat.
            if (counter == stud.size()) {
                return stud.size();
            }
        }

        return 0;
    }

}
