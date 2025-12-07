/*
GOALS: Interline v intraline
grab 2 lines XOR one over the other
to decompress, take the compressed line and XOR back with one
of the original 2 lines (very simple!)
*/

#include "mem/cache/compressors/xor.hh"

#include "base/bitfield.hh"
#include "debug/CacheComp.hh"
#include "params/Xor.hh"

namespace gem5
{
namespace compression
{

Xor::Xor(const XorParams &p) : Base(p)
{
}

std::unique_ptr<Base::CompressionData>
Xor::compress(const std::vector<Chunk>& chunks,
              Cycles& comp_lat,
              Cycles& decomp_lat)
{
    const unsigned N = chunks.size();

    auto data = std::make_unique<XorCompressionData>(N);

    if (N == 0) {
        comp_lat = decomp_lat = Cycles(0);
        return data;
    }

    data->mask.resize(N, 0);
    data->xorChunks.resize(N);

    data->xorChunks[0] = chunks[0];
    data->mask[0] = 1;

    unsigned compressedCount = 1;

    //Checks if 2 XOR equal the same value
    for (unsigned i = 1; i < N; i++) {
        uint64_t delta = chunks[i] ^ chunks[i - 1];

        if (delta == 0) {
            data->mask[i] = 0;
        } else {
            data->mask[i] = 1;
            data->xorChunks[compressedCount] = delta;
            compressedCount++;
        }
    }

    data->xorChunks.resize(compressedCount);

    data->setSizeBits(compressedCount * chunkSizeBits);

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

    const unsigned N = data->mask.size();
    if (N == 0)
        return;

    std::vector<Chunk> chunks(N);
    unsigned j = 1;

    chunks[0] = data->xorChunks[0];

    for (unsigned i = 1; i < N; i++) {
        if (data->mask[i] == 0) {
            chunks[i] = chunks[i - 1];
        } else {
            chunks[i] = data->xorChunks[j] ^ chunks[i - 1];
            j++;
        }
    }

    fromChunks(chunks, cache_line);

    DPRINTF(CacheComp,
        "XORCompressor: decompressed %u chunks\n", N);
}

} // namespace compression
} // namespace gem5
