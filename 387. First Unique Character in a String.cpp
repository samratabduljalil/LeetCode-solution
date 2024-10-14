using namespace std;
class Solution {
public:
    int firstUniqChar(string s) {
        unordered_map<char,int> string_set;
        for(int i=0;i<s.size();i++){
          string_set[s[i]]++;
        }
        for(int i=0;i<s.size();i++){
         if (string_set.find(s[i]) != string_set.end()) {
        if(string_set[s[i]] == 1) {
            return i;
        }
    } 
        }
        return -1; 
    }
};