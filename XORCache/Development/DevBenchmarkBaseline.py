# Copyright (c) 2015 Jason Power
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met: redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer;
# redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution;
# neither the name of the copyright holders nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""
This file uses the baseline 2-level cache system from gem5 for our baseline
test for cache compression

"""

# import the m5 (gem5) library created when gem5 is built
import m5

# import all of the SimObjects
from m5.objects import *
from m5.objects import TimingSimpleCPU
# Add the common scripts to our path
m5.util.addToPath('../../')

# import the caches which we made
from BaselineCaches import *

# import the SimpleOpts module
from common import SimpleOpts

# Running Benchmark
thispath = os.path.dirname(os.path.realpath(__file__))
default_binary = os.path.join(thispath, '../../../', 'tests/test-progs/DevelopmentBenchmark/x86Linux/developmentBenchmark')

# Binary to execute
SimpleOpts.add_option('binary', nargs=1)
SimpleOpts.add_option('-n', nargs=1)

# Finalize the arguments and grab the args so we can pass it on to our objects
args = SimpleOpts.parse_args()
args.binary = os.path.join(thispath, '../../../', args.binary[0])

# create the system we are going to simulate
system = System()
system.clk_domain = SrcClockDomain()
system.clk_domain.clock = '2GHz'
system.clk_domain.voltage_domain = VoltageDomain()

system.mem_mode = 'timing'
system.mem_ranges = [AddrRange('256MiB')]

# Create a CPU
system.cpu = X86TimingSimpleCPU()

# Create the L1 data cache with FPC compression
l1d = L1DCache()
l1d.compressor = Compressors.FPCD()
l1d.tags = CompressedTags()
#l1d.tags.compressor = l1d.compressor
l1d.tags.block_size = 64
l1d.tags.max_compression_ratio = 2  # Allow compression
system.cpu.dcache = l1d
system.cpu.icache = L1ICache()

# Connect cache to CPU and bus
system.membus = SystemXBar()
l1d.connectCPU(system.cpu)
system.cpu.icache.connectCPU(system.cpu)
l1d.connectBus(system.membus)
system.cpu.icache.connectBus(system.membus)


# Interrupt controller
system.cpu.createInterruptController()
system.cpu.interrupts[0].pio = system.membus.mem_side_ports
system.cpu.interrupts[0].int_requestor = system.membus.cpu_side_ports
system.cpu.interrupts[0].int_responder = system.membus.mem_side_ports

system.system_port = system.membus.cpu_side_ports

system.mem_ctrl = MemCtrl()
system.mem_ctrl.dram = DDR3_1600_8x8()
system.mem_ctrl.dram.range = system.mem_ranges[0]
system.mem_ctrl.port = system.membus.mem_side_ports

system.workload = SEWorkload.init_compatible(args.binary)
# Create a process for a simple "Hello World" application
process = Process()
# Set the command
# cmd is a list which begins with the executable (like argv)
#process.cmd = [args.binary, args.n[0]]
process.cmd = [args.binary]
# Set the cpu to use the process as its workload and create thread contexts
system.cpu.workload = process
system.cpu.createThreads()

# set up the root SimObject and start the simulation
root = Root(full_system=False, system=system)
# instantiate all of the objects we've created above
m5.instantiate()
print(f'Beginning simulation!')
exit_event = m5.simulate()
print(f'Exiting @ tick {m5.curTick()} because {exit_event.getCause()}')
