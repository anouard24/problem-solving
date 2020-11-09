// problem name: Pangram
// date:         16/01/2018

#include <stdio.h>
#include <ctype.h>
int main(int argc, char const *argv[])
{
	int n;
	scanf("%d\n",&n);
	char s[n];
	int i=0,all[26];
	while(i<n){
		scanf("%c",&s[i]);
		s[i] = tolower(s[i]);
		all[(int)(s[i]-'a')]=1;
		i++;
	}
	if(n<25){
			printf("NO\n");
			return 0;
	}
	for(i=0;i<26;i++)
		if(all[i]!=1){
			printf("NO\n");
			return 0;
		}
	printf("YES\n");
	return 0;
}

