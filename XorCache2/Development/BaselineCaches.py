"""
This file runs the development benchmark with the default cache implementation
"""

import m5
from m5.objects import Cache, Compressors, CompressedTags, ReplacementPolicies

# Add the common scripts to our path
m5.util.addToPath('../')

from common import SimpleOpts

# Some specific options for caches
# For all options see src/mem/cache/BaseCache.py

class L1Cache(Cache):
    assoc = 4
    tag_latency = 1
    data_latency = 1
    response_latency = 1
    mshrs = 8
    tgts_per_mshr = 16
    size = '2KiB'

    def connectCPU(self, cpu):
        raise NotImplementedError

    def connectBus(self, bus):
        self.mem_side = bus.cpu_side_ports

class L1ICache(L1Cache):
    def connectCPU(self, cpu):
        self.cpu_side = cpu.icache_port

class L1DCache(Cache):
    assoc = 2
    tag_latency = 1
    data_latency = 1
    response_latency = 1
    mshrs = 8
    tgts_per_mshr = 16
    size = '2KiB'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Attach the tags **after Cache.__init__**
        self.tags = CompressedTags(
            compressor = Compressors.FPCD(),
            block_size = 64,
            max_compression_ratio = 2,
            num_blocks_per_sector = 1
        )

    def connectCPU(self, cpu):
        self.cpu_side = cpu.dcache_port

    def connectBus(self, bus):
        self.mem_side = bus.cpu_side_ports