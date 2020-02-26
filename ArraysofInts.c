#include <stdio.h>
#include <stdlib.h>


int * getRandomArray(int n)
{
    int new[n];
    int i;
    for(i=0;i<n;i++)
    {
        int whoa=rand();
        new[i]=whoa;
    }
    return new;
}


int * getSortedArray(int n)
{
    printf("whoa");
    int new[n];
    int temp = n;
    int i;
    for(i=0;i<temp;i++)
    {
        new[i]=n;
        n--;
    }
    return new;
}

int main()
{
    getSortedArray(4);
    
}
