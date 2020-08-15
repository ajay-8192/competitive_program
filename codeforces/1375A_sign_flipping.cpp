#include <bits/stdc++.h>
using namespace std;

int main() {
	int test;
	cin >> test;
	while(test--){
		int n,*a;
		cin >> n;
		a = (int*)malloc(n * sizeof(int));
		for(int i = 0;i < n;i++){
			cin >> a[i];
		}
		for(int i = 0;i < n;i++){
			if (i%2 == 0){
				if(a[i] > 0) a[i] = -a[i];
			}
			else{
				if(a[i] < 0) a[i] = -a[i];
			}
		}
		for(int i = 0;i < n;i++)
			cout << a[i] << " ";
		cout << endl;
	}
	return 0;
}