#include <stdio.h>
#include <stdlib.h>
#include <time.h>
void countFivesInNElements(const int n){
    int* array = calloc(n, sizeof(int));

    //Go through all values and add increasing values
    for (int i = 0; i < n; i++){
        array[i] = i % 10;
    }

    int* count = calloc(10, sizeof(int));
    for (int i = 0; i < n; i++){
        count[array[i]]++;
    }
    printf("In list of %d, count of 5's: %d\n", n, count[5]);

    free(count);
    free(array);
}



int main(){
    srand(time(NULL));
    const int n = 100000000;
    countFivesInNElements(n);
}
