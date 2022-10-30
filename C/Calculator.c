#include <stdio.h>
int main(){
    int x, y, z;
    printf("Enter 1 for addition.\nEnter 2 for subtraction.\nEnter 3 for multiplication.\nEnter 4 for division.");
    scanf("%d",&x);
    printf("Enter the two numbers.");
    scanf("%d\n%d",&y,&z);
    switch(x){
        case 1:
            printf("%d", y+z);
            break;
        case 2:
            printf("%d", y-z);
            break;
        case 3:
            printf("%d", y*z);
            break;
        case 4:
            printf("%d", y/z);
            break;
        default:
            printf("Wrong input.");
            
    }
  return 0;
}
