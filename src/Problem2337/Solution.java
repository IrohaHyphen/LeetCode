// Accepted 12/5/2024
package Problem2337;

import java.util.HashMap;
import java.util.Collections;

class Solution {
    public boolean canChange(String start, String target) {
        HashMap<Integer, Character> startMap = new HashMap<>();
        HashMap<Integer, Character> targetMap = new HashMap<>();
        
        for (int i = 0; i < start.length(); i++) {
            if (start.charAt(i) != '_') {
                startMap.put(i, start.charAt(i));
            }
            if (target.charAt(i) != '_') {
                targetMap.put(i, target.charAt(i));
            }
        }
        
        while (!startMap.isEmpty() && !targetMap.isEmpty()) {
            // position of the most left char
            int currentStartIndex = Collections.min(startMap.keySet());
            int currentTargetIndex = Collections.min(targetMap.keySet());
            // the most left char
            char currentStartChar = startMap.get(currentStartIndex);
            char currentTargetChar = targetMap.get(currentTargetIndex);
            
            if (currentStartChar != currentTargetChar) {
                // if nth char of start and target are different
                return false;
            } else if (currentStartChar == 'L' && currentTargetIndex > currentStartIndex) {
                // if nth L of target is to the right of nth L of start
                return false;
            } else if (currentStartChar == 'R' && currentTargetIndex < currentStartIndex) {
                // if nth R of target is to the left of nth R of start
                return false;
            } else {
                // remove the most left char to check the next char
                startMap.remove(currentStartIndex);
                targetMap.remove(currentTargetIndex);
            }
        }
        
        return true;
    }
}
