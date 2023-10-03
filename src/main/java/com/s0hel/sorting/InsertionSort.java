package com.s0hel.sorting;

public class InsertionSort {

    public static int[] insertionSort(int[] arr) {
        for (int i = 1; i < arr.length; i++) {
            int j = i - 1;
            while (j >= 0 && arr[j + 1] < arr[j]) {
                // swap current and previous pointers if not sorted
                int tmp = arr[j + 1];
                arr[j + 1] = arr[j];
                arr[j] = tmp;
                // keep looping until current and previous numbers are not sorted
                j--;
            }
        }
        return arr;
    }

}
