# XORCacheCompression
## Group Members
Imran Aliji (aliji001@umn.edu)

Connor Antony (anton386@umn.edu)

Lila Craveiro (crave112@umn.edu)

Zannatun Sristy (srist001@umn.edu)

# Setup
Add all of the folders to a gem5 download, compile with 
```
scons ./build/ALL/gem5.opt -j8
```
change directory to gem5 and run 
```
make test
```
# Benchmarks
There are 4 benchmarks for testing the program. Each has a differently composed array, and a given task to complete:

1. Fill array with all zeroes except one random single value, find non-zero value
2. Fill array with sequentially increasing values, count the number of 5's
3. Fill array with random values, count the number of 5's
4. Fill array with an item every next 5th item, count the number of 5's

# Testing Benchmarks
To run all benchmarks:

  ```sh
  ./developmentBenchmark
  ```

To run specific benchmarks, include the number(s) (1-4) of the specific benchmark(s) you wish to test. The following text would run benchmarks 3 and 4:

 ```sh
  ./developmentBenchmark 3 4
  ```
