class Solution {
public:
    string addBinary(string a, string b) {
        int sizeA=a.size()-1,sizeB=b.size()-1,c=0;
string s= "";
        while(sizeA>=0 && sizeB>=0 ){
          if(b[sizeB] == '1' && a[sizeA]=='0'){
            if(c==1){
                s=s+'0';
                c=1;
            }else{
                s=s+'1';
            }
           }else if(b[sizeB] == '0' && a[sizeA]=='1'){
               if(c==1){
                s=s+'0';
                c=1;
            }else{
                s=s+'1';
            }
           }
           else if(b[sizeB] == '0' && a[sizeA]=='0'){
            if(c==1){
                s=s+'1';
                c=0;  
            }else{
                s=s+'0';  
            }
           }
           if(b[sizeB] == '1' && a[sizeA]=='1'){
             if(c==1){
                s=s+'1';
                c=1;  
            }else{
               s=s+'0';
             c=1;  
            }
            printf("%c %d",s[0],sizeB);
           }
              sizeA--;
              sizeB--;
        }
           if(c==1){
              if (sizeA>=sizeB){
               for (int k=sizeA;k>=0; k--){
                    if(a[k]=='1' && c==1){
                        s=s+'0';
                        c=1;
                    }else if(a[k]=='0' && c==0){
                        s=s+'0';
                        c=0;
                    }else if(a[k]=='0' && c==1) {
                        s=s+'1';
                        c=0;
                    }else{
                        s=s+'1';
                        c=0;
                    }     
               }
              }else{
                 for (int k=sizeB;k>=0; k--){
                    if(b[k]=='1' && c==1){
                        s=s+'0';
                        c=1;
                    }else if(b[k]=='0' && c==0){
                        s=s+'0';
                        c=0;
                    }else if(b[k]=='0' && c==1) {
                        s=s+'1';
                        c=0;
                    }else{
                        s=s+'1';
                        c=0;
                    }   
               }
              }
                        }else{
                         
                 if (sizeA>=sizeB){
               for (int k=sizeA;k>=0; k--){   
                        s=s+ a[k];      
               }
              }else{
                 for (int k=sizeB;k>=0; k--){
                     s=s+ b[k];     
               }
              }
                        }
                      if(c==1){
                        s=s+'1';
                      }  
       reverse(s.begin(), s.end());
        return s;
    }
};