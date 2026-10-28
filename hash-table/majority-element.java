class Solution {
    public int majorityElement(int[] nums) {
        int majorityElement = nums[0];
        int counter = 1;

        for(int i=1; i < nums.length; i++){
            if(counter == 0){
                majorityElement = nums[i];
                counter = 1;
            } else if(nums[i] == majorityElement){
                counter++;
            } else {
                counter--;
            }
        }
        return majorityElement;
    }
}