#include <bits/stdc++.h>
using namespace std;
// moore voting algorithm
//finding the majority element(when no. of element > size/2 + 1)
int findmajority(int arr[],int length){
    int vote = 1;
    int maj =arr[0];

    for(int i=1;i<length;i++){
        if(maj!=arr[i]) {vote--;}
        else if(maj==arr[i]) {vote++;}
        if(vote==0) {maj=arr[i];vote=1;}
    }

    return maj;
}
int main() {
    
    int arr[]={5,2,2,6,2,5,2,2,8,2};
	int majority = findmajority(arr,10);
    cout<<"majority candidate"<<majority;
	return 0;
}
