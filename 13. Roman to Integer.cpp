using namespace std;
class Solution {
public:
    int romanToInt(string s) {
        int sum=0;
        unordered_map<char, int> myMap;
         myMap['I'] = 1;
         myMap['V'] = 5;
         myMap['X'] = 10;
         myMap['L'] = 50;
         myMap['C'] = 100;
         myMap['D'] = 500;
         myMap['M'] = 1000;
         for (int i = 0; i < s.length(); i++) {
            if(s[i]=='I'){
              if(s[i+1]=='V'){
              sum=sum+4;
                i=i+1;
            }
            else if(s[i+1]=='X'){
                   sum=sum+9; 
                   i=i+1;  
            }else{
             auto it = myMap.find(s[i]);
            sum=sum+it->second;
            }
            }else if(s[i]=='X'){
              if(s[i+1]=='L'){
              sum=sum+40; 
              i=i+1;
            }
            else if(s[i+1]=='C'){
                   sum=sum+90;
                   i=i+1;  
            }else{
             auto it = myMap.find(s[i]);
            sum=sum+it->second;
            }
            } else if(s[i]=='C'){
                if(s[i+1]=='M'){
              sum=sum+900; 
              i=i+1;
            }
            else if(s[i+1]=='D'){
                   sum=sum+400; 
                   i=i+1;   
            }else{
             auto it = myMap.find(s[i]);
            sum=sum+it->second;
            }   
            } else{
         auto it = myMap.find(s[i]);
            sum=sum+it->second;
            }
         printf("%d",sum);   
    }
        return sum;
    }
};