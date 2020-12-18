#include <bits/stdc++.h>
using namespace std;
const int SZ = 50, MM = SZ+5, n = 8, m = 20;

int a[MM][MM][MM][MM];
int b[MM][MM][MM][MM];

int val(int ii, int jj, int kk, int ll){
	int cnt = 0;
	for(int i = ii-1; i <= ii+1; i++)
		for(int j = jj-1; j <= jj+1; j++)
			for(int k = kk-1; k <= kk+1; k++)
				for(int l = ll-1; l <= ll+1; l++)
					cnt += a[i][j][k][l];
	return cnt;
}

int main(){
	for(int i = m; i < m+n; i++){
		for(int j = m; j < m+n; j++)
			a[m][m][i][j] = getchar() == '#';
		getchar();
	}
	int t = 6, on;
	while(t--){
		on = 0;
		for(int i = 1; i < SZ; i++){
			for(int j = 1; j < SZ; j++){
				for(int k = 1; k < SZ; k++){
					for(int l = 1; l < SZ; l++){
						int cnt = val(i, j, k, l);
						if(a[i][j][k][l])
							b[i][j][k][l] = cnt == 3 or cnt == 4;
						else
							b[i][j][k][l] = cnt == 3;
						on += b[i][j][k][l];
					}
				}
			}
		}
		swap(a, b);
		cout<<on<<'\n';
	}
}