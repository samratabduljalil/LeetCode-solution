using namespace std;
class Solution {
public:
    char findTheDifference(string s, string t) {
       unordered_map<char, int> myMap;
       for(int i=0;i<s.size();i++){
       myMap[s[i]]++;
       }
       for(int i=0;i<t.size();i++){
       if (myMap[t[i]] > 0) {
        myMap[t[i]]--;  // Reduce the count by one
    }else {
        return t[i];
    }
       }
  return ' ';
    }
};