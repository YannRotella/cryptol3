#include<stdio.h>
#include<stdlib.h>

unsigned long long applyLFSR(unsigned long long state)
{
	printf("%llu", (state&1));
	unsigned long long mask = 1;
	mask = mask << 63;

	//VALEUR A TROUVER
	unsigned long long poly = 1;
	//

	unsigned long long scalar = poly&state;
	unsigned long long tmp = 0;
	for (int i = 0; i < 64; ++i)
	{
		tmp ^= (scalar>>i)&1;
	}
	if (tmp^1){
		return state>>1;
	}
	else {
		return (state>>1)^(mask);
	}
}

int main(int argc, char const *argv[])
{

	//VALEUR A TROUVER
	unsigned long long state = 1;
	//

	for (int i = 1; i < 141; ++i)
	{
		state = applyLFSR(state);
		if ((i%20)==0)
		{
			printf("\n");
		}
	}
	return 0;
}


