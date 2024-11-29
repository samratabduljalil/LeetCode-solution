double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size) {  
int arr[nums1Size + nums2Size],j=0,temp=0;
double median=0;
for(int i=0;i<nums1Size;i++){
arr[j]=nums1[i];
j++;
}
for(int i=0;i<nums2Size;i++){
arr[j]=nums2[i];
j++;
}
for (int i = 0; i <nums1Size + nums2Size; i++) {
        for (int j = 0; j < nums1Size + nums2Size-1; j++) {
            if(arr[j]>arr[j+1]){  
           temp=arr[j];
           arr[j]=arr[j+1];
           arr[j+1]=temp;
            }
            }
        }
if((nums1Size + nums2Size)%2==0){
    int result;
result=arr[((nums1Size + nums2Size)/2)-1]+arr[((nums1Size + nums2Size)/2)];
median=(double)result/2;
}else{
int l=ceil((nums1Size + nums2Size)/2);
median=arr[l];
}
return median;
}