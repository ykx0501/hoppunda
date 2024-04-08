#include <stdio.h>


int main(void){
    // Your code here!
    for(int a=1; a<=100; a++)
    {
        if( a%15== 0 )
        {
            printf("fizzbuzz ");
        }
        else if( a%3 == 0 )
        {
            printf("fizz ");
        }
        else if( a%5 == 0 )
        {
            printf("buzz ");
        }
        else
        {
            printf("%d ",a);
        }
    }
    
    return 0;
}
