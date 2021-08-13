#include <bits/stdc++.h>
using namespace std;

// checking two strings are anagrams or not
// anagram means all letter in one with same frequency has to be in another string
bool checkAnagram(string s1,string s2){
    if(s1.size()!=s2.size()){
        return false;
    }
    // uning map
    map<char,int> hash; 
    for(int i=0;i<s1.size();i++){
        hash[s1[i]] +=1;
        hash[s2[i]] -=1; 
    }
    for(auto letter:hash){
        if(letter.second!=0) return false;
    }
    // using vector
    // vector<int> hash(25,0);
    // for(int i=0;i<s1.size();i++){
    //     hash[s1[i]-97] +=1;
    //     hash[s2[i]-97] -=1; 
    // }
    // for(int i=0;i<hash.size();i++){
    //     if(hash[i]!=0){
    //         return false;
    //     }
    // }
    return true;
}
int main() {
    
    string s1 = "apple";
    string s2 = "aaple";
	cout<<checkAnagram(s1,s2);
	return 0;
}
