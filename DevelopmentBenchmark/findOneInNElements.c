#include <stdio.h>
#include <stdlib.h>
#include <time.h>

//Find the 0 in an array of a n elements
int findOneInNElements(const int n){
    int* array = calloc(n, sizeof(int));
    int index = rand() % n;
    array[index] = 1;

    //Go through all values and find index
    int retIndex = -1;
    for (int i = 0; i < n; i++){
        if (array[i] == 1){
            retIndex = i;
        }
    }

    printf("Element 1 found at list of %d index: %d\n",n, retIndex);
    free(array);
    return retIndex;
}

int main(){
    srand(time(NULL));
    const int n = 100000000;
    findOneInNElements(n);
}
