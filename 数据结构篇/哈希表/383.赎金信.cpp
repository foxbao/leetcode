#include <vector>
#include <iostream>
#include <unordered_set>
using namespace std;
class Solution
{
public:
    bool canConstruct(string ransomNote, string magazine)
    {
        int record[26]={};
        if (ransomNote.size() > magazine.size()) {
            return false;
        }

        for(int i=0;i<magazine.size();i++)
        {
            record[magazine[i]-'a']++;
        }
        for(int j=0;j<ransomNote.size();j++)
        {
            record[ransomNote[j]-'a']--;
            if(record[ransomNote[j]-'a'] < 0)
            {
                return false;
            }
        }
        return true;
    }

private:
};

int main()
{
    string ransomNote="aabc";
    string magazine ="aaaabbbb";
    Solution solution;
    cout<<solution.canConstruct(ransomNote,magazine);
    return 0;
}