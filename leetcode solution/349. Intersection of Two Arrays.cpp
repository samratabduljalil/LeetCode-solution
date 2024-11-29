using namespace std;
class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        unordered_set<int> my_map;
        unordered_set <int> inserted_element;
        vector<int> inserted_element_vector;
        for(int i=0;i<nums1.size();i++){
           my_map.insert(nums1[i]);
        }
        for(int i=0;i<nums2.size();i++){
           if(my_map.find(nums2[i])!=my_map.end()){
              inserted_element.insert(nums2[i]);
           }
        }
        for (auto it = inserted_element.begin(); it != inserted_element.end(); ++it) {
        inserted_element_vector.push_back(*it);
    }
        return inserted_element_vector;
    }
};