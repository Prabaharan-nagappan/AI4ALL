
# DNA Compression Techniques

import zlib
from collections import defaultdict

def enhanced_rle(dna_sequence):
    """
    Enhanced Run-Length Encoding (RLE) for DNA sequences.
    """
    encoded = []
    count = 1
    for i in range(1, len(dna_sequence)):
        if dna_sequence[i] == dna_sequence[i - 1]:
            count += 1
        else:
            encoded.append((dna_sequence[i - 1], count))
            count = 1
    encoded.append((dna_sequence[-1], count))  # Last nucleotide
    return encoded

def lzw_compress(dna_sequence):
    """
    Simple LZW Compression for DNA sequences.
    """
    dictionary = {chr(i): i for i in range(256)}  # ASCII
    output = []
    current_string = ""
    dict_size = 256

    for char in dna_sequence:
        current_string_plus_char = current_string + char
        if current_string_plus_char in dictionary:
            current_string = current_string_plus_char
        else:
            output.append(dictionary[current_string])
            dictionary[current_string_plus_char] = dict_size
            dict_size += 1
            current_string = char

    if current_string:
        output.append(dictionary[current_string])
    return output

def lzw_decompress(compressed):
    """
    Decompress LZW compressed data.
    """
    reverse_dictionary = {i: chr(i) for i in range(256)}
    result = ""
    current_string = ""
    dict_size = 256

    for code in compressed:
        if code in reverse_dictionary:
            entry = reverse_dictionary[code]
        elif code == dict_size:
            entry = current_string + current_string[0]
        result += entry

        if current_string:
            reverse_dictionary[dict_size] = current_string + entry[0]
            dict_size += 1
        current_string = entry

    return result

def benchmark_compression(dna_sequence):
    """
    Benchmark different compression techniques.
    """
    print("Original DNA Sequence:", dna_sequence)
    
    # Enhanced RLE
    rle_encoded = enhanced_rle(dna_sequence)
    print("Enhanced RLE Encoded:", rle_encoded)
    
    # LZW Compression
    lzw_encoded = lzw_compress(dna_sequence)
    print("LZW Compressed:", lzw_encoded)
    
    # Zlib Compression for comparison
    compressed_zlib = zlib.compress(dna_sequence.encode())
    print("Zlib Compressed:", compressed_zlib)

    # Decompress LZW for testing
    decompressed_lzw = lzw_decompress(lzw_encoded)
    print("Decompressed LZW:", decompressed_lzw)

if __name__ == "__main__":
    # Example DNA Sequence
    original_dna = 'CCGGTTTAAAGGGGCCGGT'
    benchmark_compression(original_dna)