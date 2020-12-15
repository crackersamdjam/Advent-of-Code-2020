#include <bits/stdc++.h>
using namespace std;
const int MM = 105;

char a[MM][MM], b[MM][MM], s[MM];
int n;
int mx[] = {1, 1, 1, 0, 0, -1, -1, -1};
int my[] = {1, 0, -1, 1, -1, 1, 0, -1};

bool equal(){
	for(int i = 1; i <= n; i++)
		for(int j = 1; j <= n; j++)
			if(a[i][j] != b[i][j])
				return 0;
	return 1;
}

void out(){
	for(int i = 1; i <= n; i++)
		printf("%s\n", a[i]+1);
	printf("\n");
}

int main(){
	for(int i = 1;; i++){
		s[1] = 0;
		scanf("%s", s+1);
		if(!s[1])
			break;
		memcpy(a[i], s, sizeof s);
		memcpy(b[i], s, sizeof s);
	}
	n = (int)strlen(a[1]+1);
	do{
		swap(a, b);
		for(int i = 1; i <= n; i++){
			for(int j = 1; j <= n; j++){
				if(a[i][j] == '.' or !a[i][j])
					continue;
				int cnt = 0;
				for(int k = 0; k < 8; k++){
					int ni = i, nj = j;
					while(1){
						ni += mx[k], nj += my[k];
						if(b[ni][nj] != '.'){
							cnt += b[ni][nj] == '#';
							break;
						}
					}
				}
				a[i][j] = b[i][j];
				if(cnt >= 5)
					a[i][j] = 'L';
				if(!cnt)
					a[i][j] = '#';
			}
		}
	} while(!equal());

	int ans = 0;
	for(int i = 1; i <= n; i++){
		for(int j = 1; j <= n; j++)
			ans += a[i][j] == '#';
	}
	printf("%d\n", ans);
}
