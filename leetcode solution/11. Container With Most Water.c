

//11. Container With Most Water

int maxArea(int* height, int heightSize) {
    int max=0,current=0,left=0,right=heightSize-1;
while(left<right){
    if(height[left]<= height[right]){
        current=height[left]*(right-left);
        left++;
        }else{
            current=height[right]*(right-left);
            right--;
            }
            if(max<current){max=current;
            }
            }
            return max;
            }