void Merge(int *arr,int high ,int low,int mid){ 
    int m=0;
    int j=0;
    int k=low,n=0;
    int arr1[mid - low + 1],arr2[high-mid];
    for(int i=0;i<mid - low + 1;i++){
        arr1[i]=arr[low+i];   
    }
      for(int i=0;i<high-mid;i++){
        arr2[i]=arr[mid + 1 + i];
        
    }
      while(m<mid - low + 1 && j<high-mid){
        if(arr1[m]<=arr2[j]){
            arr[k]=arr1[m];
            m++;
        }else{
            arr[k]=arr2[j];
            j++;
        } 
        k++;       
    }   
       for(int l=m;l<mid - low + 1;l++){
        arr[k]=arr1[l];       
        k++;
        
    }
       for(int l=j;l<high-mid;l++){
        arr[k]=arr2[l];
        k++;   
    }   
}
void MergeSort(int *arr,int low,int high){
    if(low<high){
        int mid= low + (high - low) / 2;
        MergeSort(arr,low,mid);
        MergeSort(arr,mid+1,high); 
        Merge(arr,high,low,mid);        
    }    
}
bool containsDuplicate(int* nums, int numsSize) {
 MergeSort(nums, 0, numsSize-1);
    for(int i=0;i<numsSize;i++){
          if(i!=numsSize-1){
          if(nums[i]==nums[i+1]){
            return true;
          }}else{
            return false;
          }
}
    return false;
}