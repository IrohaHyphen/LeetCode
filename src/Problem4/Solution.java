// Accepted 12/2/2024
package Problem4;

class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        double result;
        
        // first half of the hypothetical merged sorted array
        int[] newArray = new int[(nums1.length + nums2.length) / 2 + 1];
        
        int index1 = 0;
        int index2 = 0;
        
        for (int i = 0; i < newArray.length; i++) {
            if (index1 == nums1.length) {
                newArray[i] = nums2[index2++];
            } else if (index2 == nums2.length) {
                newArray[i] = nums1[index1++];
            } else if (nums1[index1] < nums2[index2]) {
                newArray[i] = nums1[index1++];
            } else {
                newArray[i] = nums2[index2++];
            }
        }
        
        if ((nums1.length + nums2.length) % 2 == 1) {
            result = newArray[newArray.length - 1];
        } else {
            result = (double) (newArray[newArray.length - 1] + newArray[newArray.length - 2]) / 2;
        }
        
        return result;
    }
}
