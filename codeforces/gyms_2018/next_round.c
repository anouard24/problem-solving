// problem name: Next Round
// date:         16/01/2018

#include <stdio.h>
int main(int argc, char const *argv[])
{
	int n,k;
	scanf("%d %d",&n,&k);
	int score[n],i=0,av=0;
	while(i<n){
		scanf("%d",&score[i]);
		if(score[i++]>0) av++;
	}
	if(score[k-1]==0){
		printf("%d\n",av);
		return 0;
	}
	i=k;
	int out = k;
	while(i<n){
		if(score[k-1] == score[i])
			if(score[k] > 0)
				out++;
		i++;
	}
	printf("%d\n",out);
	return 0;
}

