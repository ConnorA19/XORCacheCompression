#include <stdio.h>
#include <stdlib.h>
#include <time.h>

//Find the 0 in an array of a n elements
int findOneInNElements(const int n){
  printf("Running Test 4\n");
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
  printf("Running Test 1\n");
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
  printf("Running Test 3\n");
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
    printf("Running Test 2\n");
  int* array = calloc(n, sizeof(int));

  //Go through all values and add random values
  for (int i = 0; i < n; i++){
    array[i] = (rand() + 1) % 100;
  }
  
  int* count = calloc(10, sizeof(int));
  for (int i = 0; i < n; i++){
    count[array[i]]++;
  }
  printf("In list of %d, count of Random 5's: %d\n", n, count[5]);
  
  free(count);
  free(array);
}


int main(int argc, char** argv){
  srand(time(NULL));
  // for (int i = 0; i < argc; i++){
  //   printf("%s", argv[i]);
  // }
  if (argc == 2){
    int n = atoi(argv[1]);
    countFivesInNElements(n);
    countFivesInRandomNElements(n);
    countFivesInSparseNElements(n);
    findOneInNElements(n);
  }
  //1
  //countFivesInNElements(n);
  //2
  //countFivesInRandomNElements(n);
  //3
  //countFivesInSparseNElements(n);
  //4
  //findOneInNElements(n);

  else{
    int n = atoi(argv[1]);
    for (int i = 2; i < argc; i++){
      int testIdx = atoi(argv[i]);
      if (testIdx == 1) countFivesInNElements(n);
      if (testIdx == 2) countFivesInRandomNElements(n);
      if (testIdx == 3) countFivesInSparseNElements(n);
      if (testIdx == 4) findOneInNElements(n);
    }
  }
}
