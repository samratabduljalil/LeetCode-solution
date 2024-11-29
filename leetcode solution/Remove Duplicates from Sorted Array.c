
//Remove Duplicates from Sorted Array

int removeDuplicates(int* nums, int numsSize) {
int arr[numsSize];
 int flag=0,K=1,j=0;
 flag=nums[0];
 arr[0]=nums[0];
for(int i=0;i<numsSize;i++){
    
    if(i!=0){
   if(flag!=nums[i]){
     flag=nums[i];
         K++;
         j++;
     arr[j]=nums[i];
 

   }



    }
}
for(int i=0;i<K;i++){

nums[i]=arr[i];
   

   }
    
    return K;


}