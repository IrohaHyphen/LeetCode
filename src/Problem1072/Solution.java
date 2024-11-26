// Accepted 11/22/2024
package Problem1072;

import java.util.HashSet;

class Solution {
    public int maxEqualRowsAfterFlips(int[][] matrix) {
        int result = 0;
        
        var checked = new HashSet<Integer>();
        
        for (int i = 0; i < matrix.length; i++) {
            // if already part of another "equal rows" set
            if (checked.contains(i)) {
                continue;
            }
            
            int currentResult = 1;
            
            for (int j = i + 1; j < matrix.length; j++) {
                boolean equal = true;
                boolean reverse;
                
                // equal or reverse equal
                if (matrix[i][0] == matrix[j][0]) {
                    reverse = false;
                } else {
                    reverse = true;
                }
                
                for (int k = 1; k < matrix[i].length; k++) {
                    // reverse equal
                    if (!reverse && matrix[i][k] == matrix[j][k]) {
                        continue;
                    }
                    
                    // neither
                    if (!reverse && matrix[i][k] != matrix[j][k]) {
                        equal = false;
                        break;
                    }
                    
                    // equal
                    if (reverse && matrix[i][k] != matrix[j][k]) {
                        continue;
                    }
                    
                    // neither
                    if (reverse && matrix[i][k] == matrix[j][k]) {
                        equal = false;
                        break;
                    }
                }
                
                if (equal) {
                    currentResult++;
                    checked.add(j);
                }
            }
            
            result = Math.max(result, currentResult);
        }
        
        return result;
    }
}
