#include<stdio.h>
#include<stdlib.h>

int applyLFSR(int s, int p, int size)
{
	int scalar = p&s;
	int tmp = 0;
	for (int i = 0; i < size; ++i)
	{
		tmp ^= (scalar>>i)&1;
	}
	return (s>>1)^(tmp<<(size-1));
}

int f(int s, int* pos)
{
	int x0 = (s>>pos[0])&1;
	int x1 = (s>>pos[1])&1;
	int x2 = (s>>pos[2])&1;
	int x3 = (s>>pos[3])&1;
	int x4 = (s>>pos[4])&1;
	int x5 = (s>>pos[5])&1;
	int x6 = (s>>pos[6])&1;
	int r0 = (x0&x2&x5&x6)^(x0&x3&x5&x6)^(x0&x1&x5&x6)^(x0&x2&x3&x6)^(x1&x3&x4&x6);
	int r1 = (x1&x3&x5&x6)^(x0&x2&x4)^(x0&x2&x3)^(x0&x1&x3)^(x0&x2&x6)^(x0&x1&x4);
	int r2 = (x0&x1&x6)^(x1&x2&x6)^(x2&x5&x6)^(x0&x3&x5)^(x1&x4&x6)^(x1&x2&x5);
	int r3 = (x0&x3)^(x0&x5)^(x1&x3)^(x1&x5)^(x1&x6)^(x0&x2)^(x1)^(x2&x3)^(x2&x5)^(x2&x6);
	int r4 = (x4&x5)^(x5&x6)^x2^x3^x5;
	return r0^r1^r2^r3^r4;
}


int main(int argc, char const *argv[])
{
	int p1 = 0b11111111;
	int size1 = 25;
	int p2 = 0b1010111000000001;
	int size2 = 18;
	int p3 = 0b1000001010000011001;
	int size3 = 19;
	int pos1[7] = {0,4,7,9,13,14,20};
	int pos2[7] = {0,1,3,6,10,15,17};
	int pos3[7] = {0,1,2,3,12,15,17};
	
	//VALEURS A TROUVER
	int s1 = 1;
	int s2 = 1;
	int s3 = 1;
	//

	printf("%0x, %0x, %0x\n", s1, s2, s3);
	for (int i = 1; i < 101; ++i)
	{	
		int out = f(s1,pos1)^f(s2,pos2)^f(s3,pos3);
		printf("%d",out);
		s1 = applyLFSR(s1,p1,size1);
		s2 = applyLFSR(s2,p2,size2);
		s3 = applyLFSR(s3,p3,size3);
		if (i%20 == 0)
		{
			printf("\n");
		}
	}
	return 0;
}


