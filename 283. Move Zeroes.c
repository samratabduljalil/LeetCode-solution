void moveZeroes(int* nums, int numsSize) {
    int k=0;
    for(int i=0;i<numsSize;i++){
    if (nums[k]==0){
      for(int j=k;j<numsSize-1;j++){
       nums[j]=nums[j+1];
      }
      nums[numsSize-1]=0;
    }
if (nums[k]!=0){
k++;
}
  }
}