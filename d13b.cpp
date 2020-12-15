#include <bits/stdc++.h>
#define all(x) (x).begin(), (x).end()
#define gc getchar()
#define pc(x) putchar(x)
template<typename T> void scan(T &x){x = 0;bool _=0;T c=gc;_=c==45;c=_?gc:c;while(c<48||c>57)c=gc;for(;c<48||c>57;c=gc);for(;c>47&&c<58;c=gc)x=(x<<3)+(x<<1)+(c&15);x=_?-x:x;}
template<typename T> void printn(T n){bool _=0;_=n<0;n=_?-n:n;char snum[65];int i=0;do{snum[i++]=char(n%10+48);n/= 10;}while(n);--i;if (_)pc(45);while(i>=0)pc(snum[i--]);}
template<typename First, typename ... Ints> void scan(First &arg, Ints&... rest){scan(arg);scan(rest...);}
template<typename T> void print(T n){printn(n);pc(10);}
template<typename First, typename ... Ints> void print(First arg, Ints... rest){printn(arg);pc(32);print(rest...);}

using namespace std;
using ll = long long;

// Thanks Wesley

template <class T> T EEA(T a, T b, T &x, T &y){
  T xx = y = 0, yy = x = 1; while (b != 0) {
    T q = a / b; a %= b; swap(a, b);
    x -= q * xx; swap(x, xx); y -= q * yy; swap(y, yy);
  }
  if (a < 0) { a = -a; x = -x; y = -y; }
  return a;
}

template <class T> T mulInv(T a, T m) {
  T x, y; if (EEA(a, m, x, y) != 1) return -1;
  x %= m; return x < 0 ? x + m : x;
}

// Generalized Chinese Remainder Theorem to find the solution to
//   x mod lcm(a.second, b.second) given x = a.first mod a.second
//   and x = b.first mod b.second
// Template Arguments:
//   T: the type of x
// Function Arguments:
//   a: the first value and its associated mod (0 <= a.first < a.second)
//   b: the second value and its associated mod (0 <= b.first < b.second)
// Return Value: the pair x and lcm(a.second, b.second) where
//   0 <= x < lcm(a.second, b.second), x is -1 if there is no solution
// In practice, has a small constant
// Time Complexity: O(log(max(a.second, b.second)))
// Memory Complexity: O(1)
// Tested:
//   https://open.kattis.com/problems/generalchineseremainder
template <class T> pair<T, T> CRT(pair<T, T> a, pair<T, T> b) {
  T g = gcd(a.second, b.second), l = a.second / g * b.second;
  if ((b.first - a.first) % g != 0) return make_pair(-1, l);
  T A = a.second / g, B = b.second / g;
  T mul = (b.first - a.first) / g * mulInv(A % B, B) % B;
  return make_pair(((mul * a.second + a.first) % l + l) % l, l);
}

int main(){
	string s;
	cin>>s>>s;
	stringstream ss(s);
	vector<int> v;
	while(getline(ss, s, ',')){
		v.emplace_back(s == "x" ? 0 : stoll(s));
	}
	pair<ll, ll> a = {0, 1};
	for(int i = 0; i < (int)size(v); i++){
		if(v[i]){
			// cout<<v[i]<<' '<<i<<'\n';
			a = CRT(a, {-i, v[i]});
			// cout<<a.first<<' '<<a.second<<'\n';
		}
	}
	cout<<a.first<<'\n';
}