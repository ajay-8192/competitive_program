#include <bits/stdc++.h>
using namespace std;

int main() {
	int test;
	cin >> test;
	while(test--){
		int n,m;
		cin >> n >> m;
		int **a = new int*[n];
		for(int i = 0;i < n;i++) a[i] = new int[m];
		bool flag = true;
		for(int i = 0;i < n;i++){
			for(int j = 0;j < m;j++){
				cin >> a[i][j];
			}
		}
		if(!flag){
			cout << "Yes\n";
			
		}
		cout << endl;
	}
	return 0;
}