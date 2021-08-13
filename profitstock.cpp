#include <bits/stdc++.h>
using namespace std;
// finding maxium profit by purchase and sale the stocks
// and index of array defined a day of price of stock
vector<int> findProfit(int arr[],int length){
    int min = 0;
    int profit = INT_MIN;
    vector<int> day(2,0);
    for(int i=1;i<length;i++){
        if(arr[i]-arr[min]>profit){
            profit = arr[i]-arr[min];
            day[0] = min;
            day[1] = i;
        }
        if(arr[min]>arr[i]){
            min=i;
        }
    }
    return day;
}
int main() {
    
    int arr[]={5,2,6,9,8,11};
	vector<int> maxProfit = findProfit(arr,6);
    cout<<maxProfit[0]<<"-"<<maxProfit[1]<<endl;
    cout<<"max profit is: "<<arr[maxProfit[1]]-arr[maxProfit[0]];
	return 0;
}
