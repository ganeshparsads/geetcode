class Solution {
    public int numOfSubarrays(int[] arr, int k, int threshold) {
        int sum=0, subArray=0, left=0;
        for(int right=0; right<arr.length; right++){
            sum = sum + arr[right];
            while(right-left+1==k){
                if(sum/k>=threshold){
                    subArray++;
                }
                sum = sum - arr[left++];             
            }
        }
        return subArray;
    }
}