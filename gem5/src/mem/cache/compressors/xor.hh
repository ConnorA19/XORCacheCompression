

#ifndef __MEM_CACHE_COMPRESSORS_XOR_HH__
#define __MEM_CACHE_COMPRESSORS_XOR_HH__

#include "mem/cache/compressors/base.hh"
#include "params/Xor.hh"

namespace gem5
{


namespace compression
{


class Xor : public Base
{

    public:
        typedef XorParams Params;
        Xor(const XorParams &p);
        ~Xor() = default;

    protected:

        class XorCompressionData;
    
        std::unique_ptr<CompressionData> compress(
            const std::vector<Chunk>& chunks,
            Cycles& comp_lat,
            Cycles& decomp_lat
        ) override;

        void decompress(const CompressionData* comp_data,
            uint64_t* cache_line) override;

};

class Xor::XorCompressionData : public CompressionData
{
    public:
        std::vector<std::uint8_t> mask;
        std::vector<Chunk> xorChunks;

        XorCompressionData(unsigned num_chunks)
        {
            xorChunks.resize(num_chunks);
        }

        virtual ~XorCompressionData(){}
};

} // namespace compression
} // namespace gem5

#endif