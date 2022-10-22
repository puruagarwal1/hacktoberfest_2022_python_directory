#include<stdio.h> //Header File
void input(int (*ptr)[],int n,int m)
{
    int i,j;
    for(i=0;i<n;i++)
    {
        for(j=0;j<m;j++)
        scanf("%d",*(*(ptr+i)+j));
    }

}
void display(int (*p1)[],int n,int m,int (*p2)[],int x,int y)
{
    int i,j;
    for(i=0;i<n;i++)
    {
        for(j=0;j<m;j++)
        printf("%d",*(*(p1+n)+m));
        printf("\n");
    }
    for(i=0;i<x;i++)
    {
        for(j=0;j<y;j++)
        printf("%d",*(*(p2+x)+y));
        printf("\n");
    }
}
void cal()
{


}
void main() // Main Function 
{
    int i,j,x,y,n,m; //declaring variables
    printf("Enter dimensions of the 1st array: ");
    scanf("%d %d",&n,&m);
    int arr1[n][m];
    printf("Enter the elements of the 1st array: ");
    input(arr1,n,m);
    printf("Enter dimensions of the 2nd array: ");
    scanf("%d %d",&x,&y);
    int arr2[x][y];
    printf("Enter the elements of the 2nd array: ");
    input(arr2,x,y);
    display(arr1,n,m,arr2,x,y);
    if()
    
}



