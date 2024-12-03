// Accepted 12/3/2024
package Problem2109;

class Solution {
    public String addSpaces(String s, int[] spaces) {
        String result = "";
        
        for (int i = 0; i < spaces.length; i++) {
            int start = i == 0 ? 0 : spaces[i - 1];
            int end = spaces[i];
            
            result += s.substring(start, end) + " ";
            
            // on the last iteration, add the last word
            if (i == spaces.length - 1) {
                result += s.substring(end);
            }
        }
        
        return result;
    }
}
