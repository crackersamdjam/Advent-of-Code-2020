#include <bits/stdc++.h>
using namespace std;
const int MM = 1000005;

#ifndef ONLINE_JUDGE
template<typename T>
void pr(T a){std::cerr<<a<<std::endl;}
template<typename T,typename... Args>
void pr(T a, Args... args) {std::cerr<<a<<' ',pr(args...);}
#else
template<typename... Args>
void pr(Args... args){}
#endif

struct node{
	node *pre, *nx;
	int val;
};

node *a[MM];
int n, k, s[MM];

node* sub(node *l){
	if(l == a[0])
		l = a[n-1];
	else
		l = a[l->val-1];
	return l;
}

int main(){
	n = 9;
	k = 100; //k is number of moves
	string str;
	cin>>str;
	for(int i = 0; i < n; i++){
		a[i] = new node();
		s[i] = str[i]-'1';
	}
	for(int i = 0; i < n; i++){
		int l = (i-1+n)%n, r = (i+1)%n;
		a[s[i]]->val = s[i];
		a[s[i]]->pre = a[s[l]];
		a[s[i]]->nx = a[s[r]];
		// cout<<int(s[i])+1<<' '<<int(s[l])+1<<' '<<int(s[r])+1<<endl;
	}
	auto cur = a[s[0]];

	for(int t = 0; t < k; t++){
		node* b[4] = {cur->nx};
		for(int i = 1; i <= 3; i++)
			b[i] = b[i-1]->nx;
		//cur b0 b1 b2 b3	

		node* lo = sub(cur);
		while(lo->val == b[0]->val or lo->val == b[1]->val or lo->val == b[2]->val)
			lo = sub(lo);
	
		// for(int i = 0; i < n; i++){
			// cerr<<cur->val+1<<' ';
			// cur = cur->nx;
		// }
		// cerr<<endl;
		// pr("cur", cur->val+1);
		// pr("pick up", b[0]->val+1, b[1]->val+1, b[2]->val+1);
		// pr("dest", lo->val+1);

		//cut out the three
		cur->nx = b[3];
		b[3]->pre = cur;

		//add back after lo
		auto lr = lo->nx;
		lo->nx = b[0];
		b[0]->pre = lo;
		b[2]->nx = lr;
		lr->pre = b[2];
		cur = cur->nx;
	}
	cur = a[0];
	for(int i = 0; i < n-1; i++){
		cur = cur->nx;
		cout<<cur->val+1;
	}
}