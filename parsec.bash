#!bin/bash

# runTest(){
    
# 	./build/ALL/gem5.opt ./configs/XORCache/Development/DevBenchmarkBaseline.py "./tests/test-progs/DevBenchmarks/${1}" -n "${2}" -a "${3}"
#   mv ./m5out/stats.txt "../output/stats_${1}_${2}_${3}.txt"
#   echo "Wrote ../output/stats_${1}_${2}_${3}.txt"
# }
#benchmarkNames=("blackscholes" "bodytrack" "facesim" "ferret" "fluidanimate" "freqmine" "raytrace" "swaptions" "vips" "x264")
benchmarkNames=("ferret" "fluidanimate" "freqmine" "raytrace" "swaptions" "vips" "x264")

for benchmarkName in "${benchmarkNames[@]}"; do
  cd ./parsec-benchmark
  source env.sh
  parsecmgmt -a run -p ${benchmarkName} -i simsmall -s ~/XORCacheCompression/parsec-benchmark/bin/gem5Parsec
done

#for Benchmark

