//27. Remove Element


int removeElement(int* nums, int numsSize, int val) {
   int k=0,j=0;
if(numsSize!=0){
int arr[numsSize];
for(int i=0;i<numsSize;i++){
       if(nums[i]!=val){
         k++;
         arr[j]=nums[i];
         j++;
       }
    }
    for(int i=0;i<numsSize;i++){
       nums[i]=arr[i];
    }}
    return k;
}

