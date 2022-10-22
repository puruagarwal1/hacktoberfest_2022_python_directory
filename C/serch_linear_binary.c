#include<stdio.h> //Header file
void linear(int ar[], int l, int n) //function for linear search 
{
    for(int i=0;i<l;i++)
    {
        if(ar[i] == n)
        {
        printf("Found Item at index %d",i);
        exit(0); //if Element found exit the program
        }
    }
    printf("Element not found");
}
void binary(int ar[], int l, int n)//function for binary search 
{
    for(int i=0;i<=l/2;i++)
    {
        if(ar[i]==n)
        {
        printf("Found Item at index %d",n);
        exit(0);
        }
        else if(ar[l-i-1]==n)
        {
        printf("Found Item at index %d",(l-i-1));
        exit(0);
        }
    }
    printf("Element not found"); //if element not found program will print this
    
}
void main() // main function 
{
    int i,n,ch,find; //declaring variables
    printf("Enter the length of the array: ");
    scanf("%d",&n);
    int arr[n];
    printf("Enter the elements of the array: ");
    for(i=0;i<n;i++)
    scanf("%d",&arr[i]);
    printf("Enter Element to be searched: ");
    scanf("%d",&find);
    printf("Enter 1 for binary serch & 2 for linear search: ");
    scanf("%d",&ch);
    if(ch==1)
    binary(arr,n,find);
    else if(ch==2)
    linear(arr,n,find);
    else
    printf("Wrong Choice");
}