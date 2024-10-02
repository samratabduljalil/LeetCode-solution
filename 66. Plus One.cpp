class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
   int flag=0,count=digits.size()-1;
       if(digits[digits.size()-1]==9 && digits[0]==9 ){
        digits.resize(digits.size()+1);
        digits[digits.size()-1]=9;
       for(int i=0;i<digits.size();i++){
        printf(" ld %d",digits[i]);
           if(digits[i]==9){
              digits[i]=0;
           } else{
            flag=1;
            digits.resize(digits.size()-1);
            digits[i]=digits[i]+1;
           }   
       }
        printf("%d",flag);
           if(flag==0){
           digits[0]=1;
           }else{
             digits[0]=9;
           }
        digits[digits.size()-1]=0;
   }else if(digits[digits.size()-1]==9){
        for(int i=digits.size()-1;i>=0;i--){
           if(digits[i]==9 && i==count ){
              digits[i]=0;
              count--;
           }    
       }
       digits[count]=digits[count]+1;
   }else{
digits[digits.size()-1]=digits[digits.size()-1]+1;
   }
return digits;
    }
};