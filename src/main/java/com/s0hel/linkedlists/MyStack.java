package com.s0hel.linkedlists;

import java.util.LinkedList;

/**
 * Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).
 * <p>
 * Implement the MyStack class:
 * <p>
 * void push(int x) Pushes element x to the top of the stack.
 * int pop() Removes the element on the top of the stack and returns it.
 * int top() Returns the element on the top of the stack.
 * boolean empty() Returns true if the stack is empty, false otherwise.
 * Notes:
 * <p>
 * You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
 * Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.
 * <p>
 * <p>
 * Example 1:
 * <p>
 * Input
 * ["MyStack", "push", "push", "top", "pop", "empty"]
 * [[], [1], [2], [], [], []]
 * Output
 * [null, null, null, 2, 2, false]
 * <p>
 * Explanation
 * MyStack myStack = new MyStack();
 * myStack.push(1);
 * myStack.push(2);
 * myStack.top(); // return 2
 * myStack.pop(); // return 2
 * myStack.empty(); // return False
 */
public class MyStack {

    LinkedList<Integer> queue = new LinkedList<>();

    public MyStack() {
    }

    /**
     * Pushes element x to the top of the stack.
     */
    public void push(int x) {
        queue.add(x);
    }

    /**
     * Removes the element on the top of the stack and returns it.
     */
    public int pop() {
        for (int i = 0; i < queue.size() - 1; ++i) {
            queue.add(queue.pop());
        }

        return queue.pop();
    }

    public int top() {
        int top = 0;
        for (int i = 0; i < queue.size() - 1; ++i) {
            queue.add(queue.pop());
        }

        top = queue.peek();
        queue.add(queue.pop());
        return top;
    }

    public boolean empty() {
        return queue.isEmpty();
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * boolean param_4 = obj.empty();
 */
