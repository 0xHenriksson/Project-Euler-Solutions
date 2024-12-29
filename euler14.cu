/*
The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n -> 3n+1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13->40->20->10->5->16->8->4->2->1

It can be seen that this sequence (starting at 13) and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

Once the chain starts the terms are allowed to go above one million.
*/


#include <iostream>
#include <vector>
#include <algorithm>

__device__ unsigned int collatz_length(unsigned int n) {
    unsigned int length = 1;
    while (n > 1) {
        if (n % 2 == 0) {
            n /= 2;
        } else {
            n = 3 * n + 1;
        }
        length++;
    }
    return length;
}


__global__ void calculate_collatz(unsigned int* start_numbers, unsigned int* lengths, int num_numbers) {
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    if (i < num_numbers) {
        lengths[start_numbers[i]-1] = collatz_length(start_numbers[i]);
    }
}

int main() {
    const int limit = 1000000;
    std::vector<unsigned int> start_numbers(limit);
    for (unsigned int i = 0; i < limit; ++i) {
        start_numbers[i] = i + 1;
    }

    unsigned int* d_start_numbers;
    unsigned int* d_lengths;

    cudaMallocManaged(&d_start_numbers, limit * sizeof(unsigned int));
    cudaMallocManaged(&d_lengths, limit * sizeof(unsigned int));

    // Copy start numbers to device
    cudaMemcpy(d_start_numbers, start_numbers.data(), limit * sizeof(unsigned int), cudaMemcpyHostToDevice);

    int threadsPerBlock = 256;
    int blocksPerGrid = (limit + threadsPerBlock - 1) / threadsPerBlock;

    calculate_collatz<<<blocksPerGrid, threadsPerBlock>>>(d_start_numbers, d_lengths, limit);

    cudaDeviceSynchronize();

    std::vector<unsigned int> lengths(limit);
    cudaMemcpy(lengths.data(), d_lengths, limit * sizeof(unsigned int), cudaMemcpyDeviceToHost);

    unsigned int max_length = 0;
    unsigned int max_start_number = 0;
    for (unsigned int i = 0; i < limit; ++i) {
        if (lengths[i] > max_length) {
            max_length = lengths[i];
            max_start_number = i + 1;
        }
    }

    std::cout << "The starting number with the longest chain is: " << max_start_number << std::endl;
    std::cout << "The length of the chain is: " << max_length << std::endl;

    cudaFree(d_start_numbers);
    cudaFree(d_lengths);

    return 0;
}