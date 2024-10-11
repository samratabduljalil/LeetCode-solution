using namespace std;
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<char> sub_string ;
        int max=0,left=0;
        for(int right=0;right<s.size();right++){
        while(sub_string.find(s[right])!= sub_string.end()){
           sub_string.erase(s[left]);
           left++;
     }
         if(max<(right-left+1)){
            max=(right-left+1);
        }
        sub_string.insert(s[right]);
     }
        return max;
    }
};