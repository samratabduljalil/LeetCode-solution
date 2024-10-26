class Solution {
public:
    bool isValid(string s) {
        char Parentheses[s.size()];
        int j=0,flag_1st=0,flag_2nd=0,flag_3rd=0;
        for(int i=0;i<s.size();i++){
          if(s[i]=='('){
           Parentheses[j]='(';
           j++;
           flag_1st++;
          }else if(s[i]=='{'){
            Parentheses[j]='{';
           j++;
           flag_2nd++;
          }else if(s[i]=='['){
           Parentheses[j]='[';
           j++;
           flag_3rd++;
          }
          if(s[i]==')'){
            printf("%c", Parentheses[0]);
            if( Parentheses[j]=='('){
                j--;
                flag_1st--;
            }else{
                return false;
            }
          }else if(s[i]=='}'){
          if( Parentheses[j]=='{'){
                j--;
                flag_2nd--;
            }else{
                return false;
            }
          }else if(s[i]==']'){
            
            if( Parentheses[j]=='['){
                j--;
                flag_3rd--;
            }else{
                return false;
            }
          }

        }
        if(flag_1st>=1 || flag_2nd>=1 || flag_3rd>=1){
            return false;
        }
       return true; 
    }
};