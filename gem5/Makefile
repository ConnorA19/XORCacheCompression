gem5:
	scons build/ALL/gem5.opt -j8

run:
	./build/ALL/gem5.opt ./configs/XORCache/Development/DevBenchmarkBaseline.py "./tests/test-progs/DevBenchmarks/countFivesInNElements" -n "1000" -a "XOR"

test:
	./build/ALL/gem5.opt ./configs/XORCache/Development/DevBenchmarkBaseline.py "./tests/test-progs/DevBenchmarks/findOneInNElements" -n "1000" -a "XOR"
	cowsay "Splitting the output"
	grep "system.cpu.dcache.compressor.compressions" ./m5out/stats.txt
	grep "system.cpu.dcache.compressor.failedCompressions" ./m5out/stats.txt

debug:
	./build/ALL/gem5.opt --debug-flags=CacheComp ./configs/XORCache/Development/DevBenchmarkBaseline.py "./tests/test-progs/DevBenchmarks/countFivesInNElements" -n "1000" -a "XOR"

debugCompile:
	scons build/ALL/gem5.opt CPPDEFINES=DEBUG_COMPRESSION -j8