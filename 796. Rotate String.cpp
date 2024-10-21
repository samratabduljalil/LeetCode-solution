class Solution {
public:
    bool rotateString(string s, string goal) {
        int c;
        string t;
        t=t+s;
        for(int i=0;i<s.size();i++){ 
           t[0]=s[s.size()-1];
        for(int j=0;j<s.size()-1;j++){
         t[j+1]=s[j];     
        }
        cout << t << std::endl;
        if(t==goal){
            return true;   
        }else{
            s=t;
        }
        }
      return false;  
    }
};