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

void countFivesInSparseNElements(const int n){
  int* array = calloc(n, sizeof(int));

  //Go through all values and add a value every 10 elements
  for (int i = 0; i < n; i++){
    if ((i % 10) == 5){
      array[i] = i % 10;
    }
  }
  
  int* count = calloc(10, sizeof(int));
  for (int i = 0; i < n; i++){
    count[array[i]]++;
  }
  printf("In list of %d, count of sparse 5's: %d\n", n, count[5]);
  
  free(count);
  free(array);
}


void countFivesInRandomNElements(const int n){
  int* array = calloc(n, sizeof(int));

  //Go through all values and add random values
  for (int i = 0; i < n; i++){
    array[i] = (rand() + 1) % 10;
  }
  
  int* count = calloc(10, sizeof(int));
  for (int i = 0; i < n; i++){
    count[array[i]]++;
  }
  printf("In list of %d, count of Random 5's: %d\n", n, count[5]);
  
  free(count);
  free(array);
}


int main(){
  srand(time(NULL));
  const int n = 100000000;
  countFivesInNElements(n);
  countFivesInRandomNElements(n);
  countFivesInSparseNElements(n);
  findOneInNElements(n);
}
