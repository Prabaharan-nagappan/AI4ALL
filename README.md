
# DNA Compression Techniques

This repository contains a Python script implementing various DNA compression techniques, including Enhanced Run-Length Encoding (RLE) and Lempel-Ziv-Welch (LZW) compression. These methods are designed to efficiently compress DNA sequences for storage and analysis in bioinformatics.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Research Documentation](#research-documentation)
- [License](#license)

## Introduction

With the growing amount of genomic data being generated, efficient storage and transmission methods are critical. This project implements several compression techniques that can significantly reduce the size of DNA sequence data while maintaining data integrity for subsequent analysis.

## Installation

To run the compression script, you need to have Python installed. You can download Python from [python.org](https://www.python.org/downloads/).

### Required Libraries

Make sure to install the required libraries by running:

```bash
pip install zlib
```

## Usage

1. Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/dna_compression_techniques.git
cd dna_compression_techniques
```

2. Run the script:

```bash
python dna_compression_techniques.py
```

## Examples

Here's how the different compression methods work:

### Enhanced Run-Length Encoding (RLE)

The RLE method compresses sequences by replacing repeated characters with a single character followed by a count.

### Lempel-Ziv-Welch (LZW)

LZW compression works by building a dictionary of substrings encountered in the data. It replaces substrings with their dictionary indices, thus compressing the data.

### Benchmarking

The script includes a benchmarking function that compares the performance of each compression method on a sample DNA sequence.

## Research Documentation

1. **Genomic Data Storage**: Efficient compression of DNA sequences helps in reducing storage requirements, making genomic data more manageable and accessible.
2. **Bioinformatics Applications**: The techniques implemented can be used in various bioinformatics applications, including sequence alignment, variant calling, and evolutionary studies.
3. **Synthetic Biology**: As DNA data storage becomes more prevalent, these compression techniques could enhance the efficiency of synthetic DNA data storage solutions.

## Contribution

Feel free to contribute to this project by creating issues or pull requests. Your feedback and improvements are welcome!
