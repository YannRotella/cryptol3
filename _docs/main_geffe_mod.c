#include<stdio.h>
#include<stdlib.h>

int applyLFSR1(int s)
{
	int poly1 = 0b100000111;
	int scalar = poly1&s;
	int tmp = 0;
	for (int i = 0; i < 21; ++i)
	{
		tmp ^= (scalar>>i)&1;
	}
	if (tmp){
		return (s>>1)^(1<<20);
	}
	else {
		return (s>>1);
	}
}

int applyLFSR2(int s)
{
	int poly2 = 0b1010011;
	int scalar = poly2&s;
	int tmp = 0;
	for (int i = 0; i < 12; ++i)
	{
		tmp ^= (scalar>>i)&1;
	}
	if (tmp){
		return (s>>1)^(1<<11);
	}
	else {
		return (s>>1);
	}
}

int applyLFSR3(int s)
{
	int poly3 = 0b1001;
	int scalar = poly3&s;
	int tmp = 0;
	for (int i = 0; i < 17; ++i)
	{
		tmp ^= (scalar>>i)&1;
	}
	if (tmp){
		return (s>>1)^(1<<16);
	}
	else {
		return (s>>1);
	}
}

int main(int argc, char const *argv[])
{
	//VALEURS A TROUVER
	int s1 = 1;
	int s2 = 1;
	int s3 = 1;
	//
	
	for (int i = 1; i < 141; ++i)
	{
		int r = ((s2&1)&(s3&1))^(s1&1);
		s1 = applyLFSR1(s1);
		s2 = applyLFSR2(s2);
		s3 = applyLFSR3(s3);
		printf("%d",r);
		if (i%20 == 0)
		{
			printf("\n");
		}
	}
	return 0;
}


