// Accepted 11/26/2024
package Problem3;

import java.util.HashMap;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        int result = 0;
        HashMap<Character, Integer> letters = new HashMap<>();
        
        for (int i = 0; i < s.length(); i++) {
            if (letters.containsKey(s.charAt(i))) {
                result = Math.max(result, i - letters.get(s.charAt(i)));
                letters.replace(s.charAt(i), i);
            } else {
                letters.put(s.charAt(i), i);
            }
        }
        
        return result;
    }
}
