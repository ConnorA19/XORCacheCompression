#include <stdio.h>
#include <stdlib.h>
#include <time.h>


void countFivesInRandomNElements(const int n){
    printf("Running Test 2\n");
    int* array = calloc(n, sizeof(int));

    //Go through all values and add random values
    for (int i = 0; i < n; i++){
        array[i] = (rand() + 1) % 100;
    }

    int fiveCount = 0;
    for (int i = 0; i < n; i++){
        if (array[i] == 5){
            fiveCount++;
        }
    }

    printf("In list of %d, count of Random 5's: %d\n", n, fiveCount);

    free(array);
}


int main(int argc, char** argv){
    srand(time(NULL));
    int n = atoi(argv[1]);
    countFivesInRandomNElements(n);
}
