// Accepted 12/3/2024
package Problem5;

class Solution {
    public String longestPalindrome(String s) {
        String result = "";
        
        for (int i = 0; i < s.length(); i++) {
            // check for odd palindromes
            for (int j = 0; j < s.length(); j++) {
                // check for out of bounds
                if (i - j < 0) {
                    continue;
                } else if (i + j > s.length() - 1) {
                    break;
                }
                
                // if the next one is not a palindrome
                if (s.charAt(i - j) != s.charAt(i + j)) {
                    if (j * 2 - 1 > result.length()) {
                        result = s.substring(i - j + 1, i + j);
                    }
                    
                    break;
                }
            }
            
            // check for even palindromes
            for (int j = 0; j < s.length(); j++) {
                // check for out of bounds
                if (i - j < 0) {
                    continue;
                } else if (i + j + 1 > s.length() - 1) {
                    break;
                }
                
                // if the next one is not a palindrome
                if (s.charAt(i - j) != s.charAt(i + j + 1)) {
                    if (j * 2 > result.length()) {
                        result = s.substring(i - j + 1, i + j + 1);
                    }
                    
                    break;
                }
            }
        }
        
        return result;
    }
}
