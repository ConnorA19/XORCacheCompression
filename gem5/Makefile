gem5:
	scons build/ALL/gem5.opt -j8

run:
	./build/ALL/gem5.opt ./configs/XORCache/Development/DevBenchmarkBaseline.py "./tests/test-progs/DevBenchmarks/countFivesInNElements" -n "1000" -a "XOR"

test:
	./build/ALL/gem5.opt ./configs/XORCache/Development/DevBenchmarkBaseline.py "./tests/test-progs/DevBenchmarks/countFivesInNElements" -n "1000" -a "XOR"
	cowsay "Splitting the output"
	grep "system.cpu.dcache.compressor.compressions" ./m5out/stats.txt
	grep "system.cpu.dcache.compressor.failedCompressions" ./m5out/stats.txt

