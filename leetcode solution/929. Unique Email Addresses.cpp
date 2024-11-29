using namespace std;
class Solution {
public:
    int numUniqueEmails(vector<string>& emails) {
        unordered_set<string> emails_;
        for(int i=0;i<emails.size();i++){
           size_t atPos = emails[i].find('@');
           if (atPos != std::string::npos) {
       string localPart = emails[i].substr(0, atPos);
       string domainPart = emails[i].substr(atPos); 
     string cleanedLocalPart;
    for (char ch : localPart) {
        if (ch != '.') {  
            if(ch == '+'){
               break;
            }
            cleanedLocalPart += ch;
        }
    }
     emails_.insert(cleanedLocalPart+domainPart) ;
    } else {
        emails_.insert(emails[i]) ;
    }
        }
return emails_.size();
    }
};