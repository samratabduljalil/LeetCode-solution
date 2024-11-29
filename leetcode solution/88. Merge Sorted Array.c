void merge(int* nums1, int nums1Size, int m, int* nums2, int nums2Size, int n) {
int arr[nums1Size + nums2Size],j=0,temp=0;
for(int i=0;i<m;i++){
arr[j]=nums1[i];
j++;
}
for(int i=0;i<n;i++){
arr[j]=nums2[i];
j++;
}
for(int i=0;i<m+n;i++){
nums1[i]=arr[i];
}
for (int i = 0; i <m+n; i++) {
        for (int j = 0; j < m+n-1; j++) {
            if(nums1[j]>nums1[j+1]){  
           temp=nums1[j];
           nums1[j]=nums1[j+1];
           nums1[j+1]=temp;
            }
            }
        }}  