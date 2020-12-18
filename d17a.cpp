#include <bits/stdc++.h>
using namespace std;
const int SZ = 50, MM = SZ+5, n = 8, m = 20;

int a[MM][MM][MM];
int b[MM][MM][MM];

int val(int ii, int jj, int kk){
	int cnt = 0;
	for(int i = ii-1; i <= ii+1; i++)
		for(int j = jj-1; j <= jj+1; j++)
			for(int k = kk-1; k <= kk+1; k++)
				cnt += a[i][j][k];
	return cnt;
}

int main(){
	for(int i = m; i < m+n; i++){
		for(int j = m; j < m+n; j++)
			a[m][i][j] = getchar() == '#';
		getchar();
	}
	int t = 6, on;
	while(t--){
		on = 0;
		for(int i = 1; i < SZ; i++){
			for(int j = 1; j < SZ; j++){
				for(int k = 1; k < SZ; k++){
					int cnt = val(i, j, k);
					if(a[i][j][k])
						b[i][j][k] = cnt == 3 or cnt == 4;
					else
						b[i][j][k] = cnt == 3;
					on += b[i][j][k];
				}
			}
		}
		swap(a, b);
		cout<<on<<'\n';
	}
}