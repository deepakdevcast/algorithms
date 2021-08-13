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
    int count=0;
    for(int i=0;i<length;i++){
        if(arr[i]==maj){
            count++;
        }
    }

    if(count>length/2){
        return maj;
    }
    return -1;
}
int main() {
    
    int arr[]={1,2,2,1};
	int majority = findmajority(arr,5);
    cout<<"majority candidate: "<<majority;
	return 0;
}
