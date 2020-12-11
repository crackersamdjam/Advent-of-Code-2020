#include <bits/stdc++.h>
using namespace std;
const int MM = 105;

char a[MM][MM], b[MM][MM];
int n;
int mx[] = {1, 1, 1, 0, 0, -1, -1, -1};
int my[] = {1, 0, -1, 1, -1, 1, 0, -1};

bool equal(){
	for(int i = 1; i < MM; i++)
		for(int j = 1; j < MM; j++)
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
		scanf("%s", a[i]+1);
		memcpy(b[i], a[i], sizeof a[i]);
		if(!a[i][1])
			break;
	}
	do{
		swap(a, b);
		for(int i = 1; i < MM-2; i++){
			for(int j = 1; j < MM-2; j++){
				if(a[i][j] == '.' or !a[i][j])
					continue;
				int cnt = 0;
				for(int k = 0; k < 8; k++)
					cnt += b[i+mx[k]][j+my[k]] == '#';
				a[i][j] = b[i][j];
				if(cnt >= 4)
					a[i][j] = 'L';
				if(!cnt)
					a[i][j] = '#';
			}
		}
	} while(!equal());

	int ans = 0;
	for(int i = 1; i < MM-2; i++){
		for(int j = 1; j < MM-2; j++)
			ans += a[i][j] == '#';
	}
	printf("%d\n", ans);
}