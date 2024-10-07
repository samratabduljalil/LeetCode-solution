class Solution {
public:
    bool isHappy(int n) {
        std::unordered_set<int> seenNumbers;
      int m=0,k=0;
      seenNumbers.insert(n);
     while(1 ){
          k=n%10;
          n=n/10;
          m=m+k*k;
         if(m==1 && n==0){
            return true;
         }
          if (seenNumbers.find(n) != seenNumbers.end()) {
                return false;  // If m is already seen, we've entered a cycle
            }
         if(n==0){
            n=m;
            m=0;
            seenNumbers.insert(n);
         }       
     }
return false;
    }
};