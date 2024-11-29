int search(int* nums, int numsSize, int target) { 
  int low=0,high=numsSize-1;
    while(low<=high){
     if(nums[low]==target){
        return low;
     }else if (nums[high]==target){
         return high;
     }
     high--; low++;
    }
    return -1;
}