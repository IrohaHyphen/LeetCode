// Accepted 11/26/2024
package Problem2924;

import java.util.HashSet;

class Solution {
    public int findChampion(int n, int[][] edges) {
        int result = -1;
        HashSet<Integer> losers = new HashSet<>();
        
        for (int i = 0; i < n - 1; i++) {
            losers.add(edges[i][1]);
        }
        
        for (int i = 0; i < n - 1; i++) {
            if (!losers.contains(i)) {
                if (result == -1) {
                    // when first undefeated discovered
                    result = i;
                } else {
                    // if second undefeated discovered
                    result = -1;
                    break;
                }
            }
        }
        
        return result;
    }
}
