#include <bits/stdc++.h>
using namespace std;


int binarySearch(int arr[],int number,int start,int end){
    
    
    while(start<=end){
        int mid=(end+start)/2;
        if(arr[mid]==number){
            return mid;
        }
        if(arr[mid]<number){
            start = mid+1;
        }
        else{
            end = mid-1;
        }
    }
    return -1;
}
vector<vector<int>> twosum(int arr[],int size,int sum){
    vector<vector<int>> twonumber;
    // method-1
    //O(nlogn) - using sorting and searching
    // sort(arr,arr+size);
    // for(int i=0;i<size;i++){
    //     int index = binarySearch(arr,sum-arr[i],i,size-1);
    //     if(index!=-1 && index!=i){
    //         vector<int> temp;
    //         temp.push_back(arr[i]);
    //         temp.push_back(arr[index]);
    //         twonumber.push_back(temp);
    //     }
    // }

    // method-2
    sort(arr,arr+size);
    int l=0;
    int r= size-1;
    while(l<r){
        int csum = arr[l]+arr[r];
        if(csum==sum){
            vector<int> temp;
            temp.push_back(arr[l]);
            temp.push_back(arr[r]);
            twonumber.push_back(temp);
            l++;
            r--;
        }
        else if(csum<sum){
            l++;
        }
        else{
            r--;
        }
    }
    return twonumber;
}

//find subsets which as sum of 6
int sumset(int arr[],int index,vector<int> subset,int sum){
    if(sum<0 || index>4){
        return 0;
    }
    if(sum==0){
    for(auto e:subset){
        cout<<e<<" ";
    }cout<<endl;
        return 1;
    }
    subset.push_back(arr[index]);
    sumset(arr,index+1,subset,sum-arr[index]);
    subset.pop_back();
    sumset(arr,index+1,subset,sum);
    return 0;
}

int main() {
    
    int arr[]={1,2,3,3,4,5};
	vector<vector<int>> twonumber = twosum(arr,6,6);
    for(auto numbers: twonumber){
        for(auto number:numbers){
            cout<<number<<" ";
        }cout<<endl;
    }
	return 0;
}
