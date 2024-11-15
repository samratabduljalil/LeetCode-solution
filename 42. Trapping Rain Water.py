class Solution:
    def trap(self, height: List[int]) -> int:
       if not height:
            return 0
       left_pointer , right_pointer = 0,len(height)-1
       left_max ,right_max=0,0
       water_collected = 0
        
       while left_pointer < right_pointer:
            if height[left_pointer]<height[right_pointer]:
                if height[left_pointer] >= left_max:
                    left_max = height[left_pointer]
                else:
                    water_collected += left_max - height[left_pointer]
                left_pointer +=1
            else:
                if  height[right_pointer]>=right_max:
                    right_max= height[right_pointer]
                else:
                    water_collected += right_max-height[right_pointer]
                right_pointer -=1    
       return water_collected                           