// Accepted 11/22/2024
package Problem1;

import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        int firstNumber = 0;
        int secondNumber = 0;
        
        HashMap<Integer, Integer> numbers = new HashMap<>();
        
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            
            if (numbers.containsKey(complement)) {
                firstNumber = numbers.get(complement);
                secondNumber = i;
                break;
            }
            
            numbers.put(nums[i], i);
        }
        
        return new int[]{firstNumber, secondNumber};
    }
}
