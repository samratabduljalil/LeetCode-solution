class Solution {
public:
    bool checkRecord(string s) { 
        int flaga=0;
        int flagl=0;
        int flagc=1;
        int flagd=0;
        for(int i=0;i<s.size();i++){
            printf("%d",flagc);
         if(s[i]=='A'){
            if(flagl<3 && flagd==1 ){ 
            flagc=0;
            flagl=0;
            } 
            flaga++;
         }else if(s[i]=='L'){
            printf("%c",s[i]);
           if(flagc=1){
               flagl++;
               flagc=1;
               flagd=1;
           } 
         }else{
            if(flagl<3 && flagd==1 ){ 
            flagc=0;
            flagl=0;
            }
         }
        
        }
          if(flaga<2 && flagl<3){
            return true;
        }
        return false;
    }
};