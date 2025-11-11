# XORCacheCompression
## Group Members
Imran Aliji (aliji001@umn.edu)

Connor Antony (anton386@umn.edu)

Lila Craveiro (crave112@umn.edu)

Zannatun Sristy (srist001@umn.edu)

# Setup
## Python Environment
If you have a python environment already run 
```
source PATH/TO/PYVENV/bin/activate
```
If you do not have a python environment you can run
```
python -m venv PATH/TO/FOLDER/YOU/WANT/YOUR/VENV/IN
```
Once you have sourced the activate run
```
pip install -r requirements.txt
```

## Gem5

Then run: 

  ```sh
  git clone https://github.com/gem5/gem5
  ```

# Benchmarks
There are 4 benchmarks for testing the program. Each has a differently composed array, and a given task to complete:

1. Full array with all zeroes except one random single value, find non-zero value
2. Full array with sequentially increasing values, count the number of 5's
3. Full array with random values % 10, count the number of 5's
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
