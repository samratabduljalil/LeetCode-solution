using namespace std;
class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_map<int,int> duplicate;
        duplicate.insert({nums[0],0});
        for(int i=1;i<nums.size();i++){
            auto it = duplicate.find(nums[i]);
       if(it !=duplicate.end()){
           if((i-(it->second))<= k){
             return true;
           }else{
            duplicate.erase(it);
           }
       }
       duplicate.insert({nums[i],i});
        }
   return false;
    }
};