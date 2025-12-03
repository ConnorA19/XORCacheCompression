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
Move the current Gem5 configs and tests with
```
mv ./gem5 ./gem5Temp
```
Then run: 

  ```sh
  git clone https://github.com/gem5/gem5
  rm -rf ./gem5/.git
  ```
Then move configs and tests back with
```
rm -rf ./gem5/configs
rm -rf ./gem5/tests
mv ./gem5Temp/* ./gem5/
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
