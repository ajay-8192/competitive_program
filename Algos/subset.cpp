#include <bits/stdc++.h>
using namespace std;

int main(){
	// vector<int> v{1,2,3,4,5};
	/* int n = 5;
	for(int b=0;b<(1<<n);b++){
		vector<int> subset;
		for (int i=0;i<n;i++){
			if(b&(1<<i)) subset.push_back(i);
		}
		for(auto s : subset)
			cout << s << " ";
		cout << endl;
	}
	 */
	vector<int> v;
	for(int i=0;i<4;i++){
		v.push_back(i);
	}
	do{
		for (auto k : v)
			cout << k << " ";
		cout << endl;
	}while(next_permutation(v.begin(),v.end()));
}