void swap(int* a ,int* b){
    int temp=*a;
    *a=*b;
    *b=temp;  
}
int partition(int* arr,int low,int high)
{
   int i=low+1; 
    int pivot=arr[low];
    while(i<=high){
        if(pivot > arr[i]){
            i++;        
    }else if(pivot > arr[high]){
        swap(&arr[i],&arr[high]);
        high--;
    } if (pivot <= arr[high]){
        high --;}   
    }
   swap(&arr[low],&arr[high]);
   return high; 
}
void quick_sort(int* arr, int low, int high){
    if(high > low){
        int pivot = partition(arr, low, high);
        quick_sort(arr, low,  pivot-1);
        quick_sort( arr,  pivot+1, high);   
    }   
}
int missingNumber(int* nums, int numsSize) {
quick_sort(nums, 0, numsSize-1);  
for(int i=0;i<numsSize;i++){
          if(nums[i]!=i){
            return i;
          }
}
return numsSize;
}