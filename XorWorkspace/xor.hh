/**
 * @file xor.hh
 * @author Imran Aliji, Connor Antony, Lila Craveiro, Zannatun Sristy
 * @brief 
 * @version 0.1
 * @date 2025-11-18
 * 
 * @copyright Copyright (c) 2025
 * 
 */

#ifndef __MEM_CACHE_COMPRESSORS_XOR_HH__
#define __MEM_CACHE_COMPRESSORS_XOR_HH__

#include "mem/cache/compressors/base.hh"

namespace gem5
{

struct XorCacheCompressorParams;

namespace compression
{

class Xor : public Base
{

    public:
        class XorCompressionData;

        using Params = XorCacheCompressorParams;
        Xor(const Params &p);

    protected:
        std::unique_ptr<CompressionData> compress(
            const std::vector<Chunk>& chunks,
            Cycles& comp_lat,
            Cycles& decomp_lat
        ) override;

        void decompress(const CompressionData* comp_data,
        uint64_t* cache_line) override;

};

class Xor::XorCompressionData : public Base::CompressionData
{
    public:
        std::vector<Chunk> xorChunks;

        XorCompressionData(unsigned num_chunks)
        {
            xorChunks.resize(num_chunks);
        }

        virtual ~XorCompressionData(){}
};
}

Xor*
XorCacheCompressorParams::create()
{
    return new compression::Xor(this);
}

}

#endif