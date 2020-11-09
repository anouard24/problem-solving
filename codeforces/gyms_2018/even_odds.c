// problem name: Even Odds
// date:         10/11/2018

#include <stdio.h>

long long int even_odd(long long int n,long long int k){
	long long int rs,md;
	md = (long long int)((n+1)/2);
	if(k-1<md) rs = 2*k-1;
	else rs = 2*k-n-(n%2);
	return rs;
}

int main() {
	long long int n,k;
	scanf("%lld",&n);
	scanf("%lld",&k);
	printf("%lld\n",even_odd(n,k));
	return 0;
}

