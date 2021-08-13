#include <bits/stdc++.h>
using namespace std;

// checking two strings are anagrams or not
// anagram means all letter in one with same frequency has to be in another string
bool checkAnagram(string s1,string s2){
    if(s1.size()!=s2.size()){
        return false;
    }
    vector<int> hashs1(25,0);
    vector<int> hashs2(25,0);
    for(int i=0;i<s1.size();i++){
        hashs1[s1[i]-97] +=1;
        hashs2[s2[i]-97] +=1; 
    }
    for(int i=0;i<hashs1.size();i++){
        if(hashs1[i]!=hashs2[i]){
            return false;
        }
    }
    return true;
}
int main() {
    
    string s1 = "apple";
    string s2 = "paple";
	cout<<checkAnagram(s1,s2);
	return 0;
}
