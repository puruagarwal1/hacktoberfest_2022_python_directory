#include<stdio.h> //Header File
void main() // Main Function 
{
    int i,j,n,m; //declaring variables
    printf("Enter dimensions of the array: ");
    scanf("%d %d",&n,&m);
    int arr[n][m];
    printf("Enter the elements of the array: ");
    for(i=0;i<n;i++)
    {
        for(j=0;j<m;j++)
        scanf("%d",&arr[i][j]);
    }
    printf("Entered 2D matrix is:\n");
    for(i=0;i<n;i++)
    {
        for(j=0;j<m;j++)
        {
        printf("%d ",*(*(arr+i)+j)); //traversing 2D array using pointers
        }
        printf("\n");
    }    
}