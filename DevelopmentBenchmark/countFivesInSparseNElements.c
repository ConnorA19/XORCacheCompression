#include <stdio.h>
#include <stdlib.h>
#include <time.h>


void countFivesInSparseNElements(const int n){
    printf("Running Test 3\n");
    int* array = calloc(n, sizeof(int));

    //Go through all values and add a value every 10 elements
    for (int i = 0; i < n; i++){
        if ((i % 10) == 5){
            array[i] = i % 10;
        }
    }
    int fiveCount = 0;
    for (int i = 0; i < n; i++){
        if (array[i] == 5){
            fiveCount++;
        }
    }
    printf("In list of %d, count of sparse 5's: %d\n", n, fiveCount);

    free(array);
}



int main(int argc, char** argv){
    srand(time(NULL));
    int n = atoi(argv[1]);
    countFivesInSparseNElements(n);
}
