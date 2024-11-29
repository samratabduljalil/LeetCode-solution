//Two Sum

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
 int* arr = (int*)malloc(2 * sizeof(int));
 int flag=NULL;
for(int i=0;i<numsSize;i++){
if(i<numsSize-1){
if((nums[i]+nums[i+1]== target)){
 arr[0] =i;
 arr[1] =i+1;
 flag=1;


}
}
 if (flag == NULL){
for(int i=0;i<numsSize;i++){
    for(int j=i+1;j<numsSize;j++){
if((nums[i]+nums[j]== target)){
 arr[0] =i;
 arr[1] =j;



}
    }}
}

}
*returnSize = 2; 
    return arr;
}