using namespace std;
class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
         unordered_map<char, int> Magazine_char;
       for(int i=0;i<magazine.size();i++){
                Magazine_char[magazine[i]]++;
       }
  int flag=0;
       for(int i=0;i<ransomNote.size();i++){
      if (Magazine_char[ransomNote[i]] > 0) {
                Magazine_char[ransomNote[i]]--;
                flag++; // Use one occurrence of the character
            } 
       }
       if(ransomNote.size()==flag){
        return true;
       }
  return false;
    }
};