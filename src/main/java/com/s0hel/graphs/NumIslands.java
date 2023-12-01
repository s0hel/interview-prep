package com.s0hel.graphs;

import java.util.*;

public class NumIslands {


    private static class Pair {
        int row;
        int column;

        public Pair(int row, int column) {
            this.row = row;
            this.column = column;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            Pair pair = (Pair) o;
            return row == pair.row && column == pair.column;
        }

        @Override
        public int hashCode() {
            return Objects.hash(row, column);
        }
    }

    public int numIslands(char[][] grid) {
        Set<Pair> visited = new HashSet<>();

        int ROWS = grid.length;
        int COLUMNS = grid[0].length;

        int islandCounter = 0;
        for (int row = 0; row < grid.length; ++row) {
            for (int column = 0; column < grid[row].length; ++column) {
                char point = grid[row][column];
                Pair coordinates = new Pair(row, column);
                if (point == '1' && !visited.contains(coordinates)) {

                    visitIsland(coordinates, visited, grid);
                    islandCounter++;
                }
            }
        }

        return islandCounter;
    }

    void visitIsland(Pair coordinates, Set<Pair> visited, char[][] grid) {

        int ROWS = grid.length;
        int COLUMNS = grid[0].length;

        Queue<Pair> queue = new LinkedList<>();
        visited.add(coordinates);

        queue.add(coordinates);

        while (!queue.isEmpty()) {
            Pair coord = queue.poll();
            int row = coord.row;
            int column = coord.column;

            // check neighbors
            List<Pair> toCheck = new ArrayList<>();
            toCheck.add(new Pair(row - 1, column));
            toCheck.add(new Pair(row + 1, column));
            toCheck.add(new Pair(row, column + 1));
            toCheck.add(new Pair(row, column - 1));

            for (Pair next : toCheck) {
                if (next.row >= 0
                        && next.row < ROWS
                        && next.column >= 0
                        && next.column < COLUMNS
                        && grid[next.row][next.column] == '1'
                        && !visited.contains(next)) {
                    queue.add(next);
                    visited.add(next);
                }
            }
        }

    }
}
