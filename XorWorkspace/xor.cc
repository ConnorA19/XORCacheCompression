/*
GOALS: Interline v intraline
grab 2 lines XOR one over the other
to decompress, take the compressed line and XOR back with one
of the original 2 lines (very simple!)
*/


#include "mem/cache/compressors/xor.hh"


#include "base/bitfield.hh"
#include "debug/CacheComp.hh"
#include "params/xor.hh"

namespace gem5
{
namespace compression
{

xor::xor(const Params &p) : Base(p){}

std::unique_ptr<Base::CompressionData>
xor::compress(const std::vector<Chunk>& chunks,
            Cycles& comp_lat,
            Cycles& decomp_lat)
{
    const unsigne N = chunks.size();
    auto data = std::make_unique<XorCompressionData>(N);

    if (N == 0) {
        comp_lat = decomp_lat = Cycles(0);
        return data;
    }

    data->xorChunks[0] = chunks[0];

    for (unsigned i = 1; i < N; i++){
        data->xorChunks[i] = chunks[i] ^ chunks[i - 1];
    }

    data->setSizeBits(N * chunkSizeBits);

    comp_lat = Cycles(divCeil(N, compChunksPerCycle)) + compExtraLatency;
    decomp_lat = Cycles(divCeil(N, decompChunksPerCycle)) + decompExtraLatency;

    DPRINTF(CacheComp, 
        "XORCompressor: compressed %u chunks, sizeBits=%u\n",
        N, data->getSizeBits());

    return data;

}

void Xor::decompress(const CompressionData* comp_data,
        uint64_t* cache_line)
{
    auto* data = static_cast<const XorCompressionData*>(comp_data);

    const unsigned N = data->xorChunks.size();
    if (N == 0)
        return;
    
    std::vector<Chunk> chunks(N);

    chunks[0] = data->xorChunks[0];
    for (unsigned i = 1; i < N; i++) {
        chunks[i] = data->xorChunks[i] ^ chunks[i - 1];
    }

    fromChunks(chunks, cache_line);

    DPRINTF(CacheComp,
    "XORCompressor: decompressed %u chunks\n", N);
}

}


}