// Accepted 12/2/2024
package Problem1455;

class Solution {
    public int isPrefixOfWord(String sentence, String searchWord) {
        int result = -1;
        
        String[] words = sentence.split(" ");
        
        for (int i = 0; i < words.length; i++) {
            if (words[i].startsWith(searchWord)) {
                result = i + 1;
                break;
            }
        }
        
        return result;
    }
}
