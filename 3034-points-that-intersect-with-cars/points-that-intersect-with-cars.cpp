class Solution {
public:
    int numberOfPoints(vector<vector<int>>& nums) {
        int freq[101] = {0};
        for(auto x: nums){
            for(int i = x[0];i <= x[1];i++){
                freq[i]++;
            }
        }
        int count = 0;
        for(int i = 1;i <= 100;i++){
            if(freq[i] > 0)
            count++;
        }
        return count;
        
    }
};