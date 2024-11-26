// Accepted 11/22/2024
package Problem2257;

class Solution {
    public int countUnguarded(int m, int n, int[][] guards, int[][] walls) {
        int result = 0;
        
        boolean[][] unguarded = new boolean[m][n];
        boolean[][] obstacles = new boolean[m][n];
        
        // default value
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                unguarded[i][j] = true;
                obstacles[i][j] = false;
            }
        }
        
        // on top of walls
        for (int i = 0; i < walls.length; i++) {
            unguarded[walls[i][0]][walls[i][1]] = false;
            obstacles[walls[i][0]][walls[i][1]] = true;
        }
        
        // on top of guards
        for (int i = 0; i < guards.length; i++) {
            unguarded[guards[i][0]][guards[i][1]] = false;
            obstacles[guards[i][0]][guards[i][1]] = true;
        }
        
        // check each guard's line of sights
        for (int i = 0; i < guards.length; i++) {
            int x = guards[i][0];
            int y = guards[i][1];
            
            // north line of sight
            for (int north = y + 1; north < n; north++) {
                if (!obstacles[x][north]) {
                    unguarded[x][north] = false;
                } else {
                    break;
                }
            }
            
            // south line of sight
            for (int south = y - 1; south >= 0; south--) {
                if (!obstacles[x][south]) {
                    unguarded[x][south] = false;
                } else {
                    break;
                }
            }
            
            // east line of sight
            for (int east = x + 1; east < m; east++) {
                if (!obstacles[east][y]) {
                    unguarded[east][y] = false;
                } else {
                    break;
                }
            }
            
            // west line of sight
            for (int west = x - 1; west >= 0; west--) {
                if (!obstacles[west][y]) {
                    unguarded[west][y] = false;
                } else {
                    break;
                }
            }
        }
        
        // count unguarded cells
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (unguarded[i][j]) {
                    result++;
                }
            }
        }
        
        return result;
    }
}
