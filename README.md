# XORCacheCompression
## Group Members
Imran Aliji (aliji001@umn.edu)

Connor Antony (anton386@umn.edu)

Lila Craveiro (crave112@umn.edu)

Zannatun Sristy (srist001@umn.edu)

# Setup
To activate python or gem5 run: 
  ```sh
  source startUp.sh
  ```
This will set up a virtual environment for running the code.

Then run: 

  ```sh
  git clone https://github.com/gem5/gem5
  ```

# Benchmarks
There are 4 benchmarks for testing the program. Each has a differently composed array, and a given task to complete:

1. Fill array with all zeroes except one random single value, find non-zero value
2. Fill array with sequentially increasing values, count the number of 5's
3. Fill array with random values % 10, count the number of 5's
4. Fill array with a 5 every 10th value of zeroes

# Testing Benchmarks
To run all benchmarks:

  ```sh
  ./developmentBenchark
  ```

To run specific benchmarks, include the number(s) (1-4) of the specific benchmark(s) you wish to test. The following text would run benchmarks 3 and 4:

 ```sh
  ./developmentBenchark 3 4
  ```
